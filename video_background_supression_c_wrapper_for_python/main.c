// gcc main.c -I/usr/include/python3.8/ -lpython3.8
#include<stdio.h>
#include<stdlib.h>
#include<stdint.h>
#include<assert.h>

#include"Python.h"

#include"interface.h"

struct API api;   /* global var */
#define VIDEO_WIDTH 288
#define VIDEO_HEIGHT 352

typedef struct videoInfo{
  FILE *fp;
  long int fileSize;
  int frameSize;
  int height;
  int width;
  int frameCnt;	
}videoInfo;
videoInfo v;

int openFile(const char *filename)
{

  v.fp = fopen(filename, "rb");
  if(!v.fp)
  {
    perror("Error opening yuv image for read");
    return -1;
  }
  /* Finding size of file */
  fseek(v.fp, 0, SEEK_END);
  v.fileSize = ftell(v.fp);  
  v.frameCnt = 0;
  v.width  = VIDEO_WIDTH;
  v.height = VIDEO_HEIGHT;
  v.frameSize = v.width * v.height * 3 / 2; //152064;
  printf("File size %ld width %d, height %d, frameSize %d\n",v.fileSize, v.width, v.height, v.frameSize); 
  printf("Total frames %ld\n",(v.fileSize/v.frameSize));
}  

/*read YUV frame */
int readRawYUV(uint32_t width, uint32_t height, uint8_t **YUV)
{

  fseek(v.fp, v.frameCnt, SEEK_SET);

  *YUV = malloc(v.frameSize);
  
  size_t result = fread(*YUV, 1, v.frameSize, v.fp);
  if (result != v.frameSize) 
  {
    perror("Error reading yuv image");
    fclose(v.fp);
    return 3;
  }
}

/*main start */
int main(void)
{
  int rc;
  uint8_t *YUV;
  PyObject *pName, *pModule, *py_results;
  PyObject *fill_api;
  #define PYVERIFY(exp) if ((exp) == 0) { fprintf(stderr, "%s[%d]: ", __FILE__, __LINE__); PyErr_Print(); exit(1); }
  
  //Py_SetProgramName(argv[0]);  /* optional but recommended */
  Py_Initialize();
  PyRun_SimpleString(
            "import sys;"
            "sys.path.insert(0, '.')" );

  PYVERIFY( pName = PyUnicode_FromString("bgSup") ) //python interface file
  PYVERIFY( pModule = PyImport_Import(pName) )
  Py_DECREF(pName);
  PYVERIFY( fill_api = PyObject_GetAttrString(pModule, "fill_api") )
  PYVERIFY( py_results = PyObject_CallFunction(fill_api, "k", &api) )
  assert(py_results == Py_None);

  int ret = openFile("out.yuv");
  if(ret<0)
  {
    return -1;
  }
  
  for(int ii=0; ii<(v.fileSize/v.frameSize); ii++)
  {	
    if(readRawYUV(v.width, v.height, &YUV) < 0)
    {
      printf("readRawYUV failed!!!\n");
    }
    /* calling python function */
    api.startStream(YUV, v.frameSize, v.width, v.height);
    v.frameCnt = v.frameCnt + v.frameSize;
    free(YUV);
  }
  
  if(YUV != NULL)
    free(YUV);
  fclose(v.fp);
  // Close Python interpreter.
  Py_Finalize();
  
  return 0;
}

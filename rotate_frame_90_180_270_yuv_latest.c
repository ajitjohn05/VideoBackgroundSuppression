#include <stdio.h>
#include <stdlib.h>

//====================================== rotate 90 =============================
void rotateLumaDegree90(unsigned char *des, unsigned char *src,int width, int height)
{
	int iIndex1 = 0;
	int iIndex2 = 0;
	
	//for luma
	for(iIndex1=0; iIndex1 < height; iIndex1++)
	{
		unsigned char* pucTempSrc = src + iIndex1 * width;
		unsigned char* pucTempDst = des + height - 1 - iIndex1;
		for (iIndex2 = 0; iIndex2 < width; iIndex2++)
		{
			*pucTempDst = *pucTempSrc;

			pucTempSrc++;
			pucTempDst += height;
		}
	}
}

void rotateChromaDegree90(unsigned char* desUV, unsigned char* srcUV, int widthUV, int heightUV)
{
	int iIndex1 = 0;
	int iIndex2 = 0;

	unsigned char* desU = desUV;
	unsigned char* desV = desUV + (widthUV * heightUV);

	unsigned char* srcU = srcUV;
	unsigned char* srcV = srcUV + (widthUV * heightUV);

	//for luma
	for (iIndex1 = 0; iIndex1 < heightUV; iIndex1++)
	{
		unsigned char* pucTempSrcU = srcU + iIndex1 * widthUV;
		unsigned char* pucTempDstU = desU + heightUV - 1 - iIndex1;

		unsigned char* pucTempSrcV = srcV + iIndex1 * widthUV;
		unsigned char* pucTempDstV = desV + heightUV - 1 - iIndex1;

		for (iIndex2 = 0; iIndex2 < widthUV; iIndex2++)
		{
			// U
			*pucTempDstU = *pucTempSrcU;
			pucTempSrcU++;
			pucTempDstU += heightUV;

			// V
			*pucTempDstV = *pucTempSrcV;
			pucTempSrcV++;
			pucTempDstV += heightUV;
		}
	}
}

void rotateYUV420Degree90(unsigned char* des, unsigned char* src, int width, int height)
{
	unsigned char* desUV = des + (width * height);
	unsigned char* srcUV = src + (width * height);
	int widthUV = width>>1;
	int heightUV = height>>1;

	// rotate luma
	rotateLumaDegree90(des, src, width, height);

	// rotate chroma
	rotateChromaDegree90(desUV, srcUV, widthUV, heightUV);
}
//=========================== rotate 90 END HERE ===============================

//====================================== rotate 270 ============================
void rotateLumaDegree180(unsigned char* des, unsigned char* src, int width, int height)
{
	int iIndex1 = 0;
	int iFrameSize = (width * height);

	unsigned char* pucTempSrc = src;
	unsigned char* pucTempDst = des + iFrameSize - 1;


	//for luma
	for (iIndex1 = 0; iIndex1 < iFrameSize; iIndex1++)
	{
		*pucTempDst = *pucTempSrc;

		pucTempSrc++;
		pucTempDst--;
	}
}

void rotateChromaDegree180(unsigned char* desUV, unsigned char* srcUV, int widthUV, int heightUV)
{
	int iIndex1 = 0;
	int iFrameSizeUV = (widthUV * heightUV);

	unsigned char* desU = desUV + iFrameSizeUV - 1;
	unsigned char* desV = desU + iFrameSizeUV;

	unsigned char* srcU = srcUV;
	unsigned char* srcV = srcUV + iFrameSizeUV;

	for (iIndex1 = 0; iIndex1 < iFrameSizeUV; iIndex1++)
	{
		//U
		*desU = *srcU;
		srcU++;
		desU--;

		// V
		*desV = *srcV;
		srcV++;
		desV--;
	}
}

void rotateYUV420Degree180(unsigned char* des, unsigned char* src, int width, int height)
{
	unsigned char* desUV = des + (width * height);
	unsigned char* srcUV = src + (width * height);
	int widthUV = width >> 1;
	int heightUV = height >> 1;

	// rotate luma
	rotateLumaDegree180(des, src, width, height);

	// rotate chroma
	rotateChromaDegree180(desUV, srcUV, widthUV, heightUV);
}
//=========================== rotate 180 END HERE ==============================

//====================================== rotate 270 ============================
void rotateLumaDegree270(unsigned char* des, unsigned char* src, int width, int height)
{
	int iIndex1 = 0;
	int iIndex2 = 0;
	int iOffset = (width * height) - height;

	//for luma
	for (iIndex1 = 0; iIndex1 < height; iIndex1++)
	{
		unsigned char* pucTempSrc = src + iIndex1 * width;
		unsigned char* pucTempDst = des + iOffset + iIndex1;
		for (iIndex2 = 0; iIndex2 < width; iIndex2++)
		{
			*pucTempDst = *pucTempSrc;

			pucTempSrc++;
			pucTempDst -= height;
		}
	}
}

void rotateChromaDegree270(unsigned char* desUV, unsigned char* srcUV, int widthUV, int heightUV)
{
	int iIndex1 = 0;
	int iIndex2 = 0;
	int iOffset = (widthUV * heightUV) - heightUV;

	unsigned char* desU = desUV;
	unsigned char* desV = desUV + (widthUV * heightUV);

	unsigned char* srcU = srcUV;
	unsigned char* srcV = srcUV + (widthUV * heightUV);

	//for luma
	for (iIndex1 = 0; iIndex1 < heightUV; iIndex1++)
	{
		unsigned char* pucTempSrcU = srcU + iIndex1 * widthUV;
		unsigned char* pucTempDstU = desU + iOffset + iIndex1;

		unsigned char* pucTempSrcV = srcV + iIndex1 * widthUV;
		unsigned char* pucTempDstV = desV + iOffset + iIndex1;

		for (iIndex2 = 0; iIndex2 < widthUV; iIndex2++)
		{
			// U
			*pucTempDstU = *pucTempSrcU;
			pucTempSrcU++;
			pucTempDstU -= heightUV;

			// V
			*pucTempDstV = *pucTempSrcV;
			pucTempSrcV++;
			pucTempDstV -= heightUV;
		}
	}
}

void rotateYUV420Degree270(unsigned char* des, unsigned char* src, int width, int height)
{
	unsigned char* desUV = des + (width * height);
	unsigned char* srcUV = src + (width * height);
	int widthUV = width >> 1;
	int heightUV = height >> 1;

	// rotate luma
	rotateLumaDegree270(des, src, width, height);

	// rotate chroma
	rotateChromaDegree270(desUV, srcUV, widthUV, heightUV);
}
//=========================== rotate 270 END HERE ==============================

int main()
{
	int width = 352;
	int height = 288;
	int framesize = (width * height * 3) >> 1;

	FILE* fIn = NULL;
	FILE* fOut_90 = NULL;
	FILE* fOut_270 = NULL;
	FILE* fOut_180 = NULL;

	unsigned char* inbuf = NULL;
	unsigned char* outbuf = NULL;

	// open Input File
	fIn = fopen("input_352x288_P420.yuv","rb");
	if(NULL == fIn)
	{
		printf("fIn : File open failed \n");
		goto END;
	}
	
	// open Output file 90
	fOut_90 = fopen("rotate90_288x352_P420.yuv", "wb");
	if(NULL == fOut_90)
	{
		printf("fOut_90 : File open failed \n");
		goto END;
	}

	// open Output file 180
	fOut_180 = fopen("rotate180_352x288_P420.yuv", "wb");
	if (NULL == fOut_180)
	{
		printf("fOut_180 : File open failed \n");
		goto END;
	}

	// open Output file 270
	fOut_270 = fopen("rotate270_288x352_P420.yuv", "wb");
	if (NULL == fOut_270)
	{
		printf("fOut_270 : File open failed \n");
		goto END;
	}

	// allocate input buffer
	inbuf=(unsigned char *)malloc(sizeof(unsigned char)*framesize);
	if(NULL == inbuf)
	{
		printf("Malloc fialed\n");
		goto END;
	}

	// allocate output buffer
	outbuf=(unsigned char *)malloc(sizeof(unsigned char)*framesize);
	if(NULL == outbuf)
	{
		printf("Malloc fialed\n");
		goto END;
	}

	// read one frame 
	fread(inbuf, framesize, 1, fIn);

	// rotate by 90 and wriet to file 
	rotateYUV420Degree90(outbuf, inbuf, width, height);
	fwrite(outbuf, framesize, 1, fOut_90);

	// rotate by 180 and wriet to file 
	rotateYUV420Degree180(outbuf, inbuf, width, height);
	fwrite(outbuf, framesize, 1, fOut_180);

	// rotate by 270 and wriet to file 
	rotateYUV420Degree270(outbuf, inbuf, width, height);
	fwrite(outbuf, framesize, 1, fOut_270);
	
END:
	if (fIn) fclose(fIn);
	if (fOut_90) fclose(fOut_90);
	if (fOut_180)
	{
		fclose(fOut_180);
	}
	
	if (fOut_270) fclose(fOut_270);

	if (inbuf) free(inbuf);
	if (outbuf) free(outbuf);
	
	return 0;
}
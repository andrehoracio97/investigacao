int main(int argc, char *argv[]) {
	float value=1100;
	float result=0;
	for (int i = 1; i < 64; ++i)
	{
		result=value/i;
		printf("I%d = %f\n",i,result);
	}

}
int compare (const void * a, const void * b)
{
  	return ( *(int*)a - *(int*)b );
}

qsort (W, N, sizeof(int), compare);
#include <stdio.h>

int tmp[1000000] = { 0 };
void merge(int arr[], int p, int q, int r) {
    int i = p, j = q + 1, k = p;
    
    while (i <= q || j <= r) {
      if (i > q) tmp[k++] = arr[j++];
      else if (j > r) tmp[k++] = arr[i++];
      else if (arr[i] <= arr[j]) tmp[k++] = arr[i++];
      else tmp[k++] = arr[j++];
    }
    for (int i = p; i <= r; i++) arr[i] = tmp[i];
}

void mergeSort(int arr[], int p, int r) {
    if (p < r) {
        int q = (p + r) / 2;
        mergeSort(arr, p, q);
        mergeSort(arr, q + 1, r);
        merge(arr, p, q, r);
    }
}

int main()
{
	int i,num = 0;
	scanf("%d", &num);
	int arr[num];
  
	for (i=0; i<num; i++){	
    scanf("%d",&arr[i]);
	}
  
	mergeSort (arr,0,num-1);
	for (i=0; i<num; i++){	
    printf("%d\n",arr[i]);
	}
	
	return 0;
}

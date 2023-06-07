#include <stdio.h>
#include<bits/stdc++.h>

int main(){

  int arr[5] = {1, 5, 2, 4, 5};
  int len = sizeof(arr)/sizeof(int);
  for (int i=0; i < len ; i++){
    for (int j =0 ; j < len - i - 1; j++){
      if (arr[j] > arr[j+1]){
        int temp = arr[j];
            arr[j] = arr[j+1];
            arr[j+1] = temp;
      }
      
    }
  }
  for (int k = 0 ; k < len; k++ ){
    printf("%d ", arr[k]);
  }
  sort(arr, arr+5);
}
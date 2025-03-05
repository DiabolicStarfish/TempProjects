#include <iostream>

int main(){
    int x[3];
    char y[2];
    int i;
    int ans=0;

    std::cout<<"Hello World!";
    for(i=0; i<3; i++){
        std::cout<<"\nInput the ["<<i+1<<"] number: ";
        std::cin>>x[i];
    }
    std::cout<<"\nChoose what operation to do: ";
    for(int j=0; j<i-1; j++){
        std::cout<<"\nFor the ["<<j+1<<"] pair: ";
        std::cin>>y[j];
    }

    for(int k=0; k<3; k++){
        std::cout<<x[k];
        if(k<2){
            std::cout<<y[k];
        }
    }

    for(int j=0; j<3; j++){
        if(y[j] == '+'){
            ans = ans + x[j];
        }
        else if(y[j] == '-'){
            ans = ans - x[j];
        }
        else if(y[j] == '*'){
            ans = ans * x[j];
        }
        else if(y[j] == '/'){
            ans = ans / x[j];
        }
        else{
            std::cout<<"\nInvalid operation!!!";
        }
    }
    std::cout<<"= "<<ans;    
    return 0;
}
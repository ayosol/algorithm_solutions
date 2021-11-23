
function isPalindrome (str){
    let j = str.length - 1;
     for (let i = 0; i < j/2; i++){
         let a = str[i];
         let b = str[j-i];

         if (a != b){
             return false;
         }

     }
     return true;
}

function checkIfpalindrome(num){
    let str_num = num.toString();
    let check_palindrome = isPalindrome(str_num);
    if (check_palindrome === true)
    {
        console.log("Number is a Palindrome");
    }
    else {
        console.log("Number is not a Palindrome");
    }
}


let x = 10021001;
checkIfpalindrome(x);
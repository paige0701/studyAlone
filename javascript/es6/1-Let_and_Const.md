<h3>1. Let and Const </h3>

Let은 scope 가 있다. Block 안에서 선언했다면 밖에서 사용할 수 없다
Let has a blocked scope. If you declared a variable with let inside a block, you cannot use it outside of the blocked scope.

eg)
```
let a = 0;
if (a === 0) {

 let b = 'hi';
 console.log(a); // 0
 console.log(b); // hi
 
}

console.log(b) // error
console.log(a) // 0
```

Const 는 값을 할당하면 바꿀수 없다.
You can't change the value of const.


Const를 사용해서 변수를 선언할 경우 초기값이 있어야 한다.
Must declare initial value when declaring a const variable. 

eg)
```
const a = 10;
const b = {name : 'paige', age : 20}
if (a === 10) {

 a = 20; // error
 b.name = 'Bonnie'; // ok 
 b['gender'] = 'female' // ok
 console.log(b) // {name: 'Bonnie', age : 20, gender:'female'}
 
 b = {birthdayMonth : 'July'} // 불가능  

}
```
여기서 b.name = 'Jenny'로 바꿀수 있는 이유는 
const b = 는 {} 이기 때문이다. 
{} 안에 있는 값은 바꿀수 있음. 
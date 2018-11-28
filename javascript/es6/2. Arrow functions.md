Arrow functions

old version without parameter
```
function func1() {
 console.log('Hi')
}

func1() // hi

```

new version without parameter
```
let func2 = () => {
 console.log('hi')
}

func2() // hi
```

old version with parameter
```
function func3(a, b) {
 console.log(a+b);
} 

func3(1,2) // 3
```

new version with parameter
```
let func4 = (a,b) => {
 console.log(a+b)
}

func(2,3) // 5

let func4 = a => a * 2  // you can omit the curly braces

func4(10) // 20 
```

Default parameter
```
let func5 = (a,b = 10) => {
 console.log(a+b)
}

func5(10) // 20
func5(10,20) // 30

let func6 = (a = 10,b) => {
 console.log(a+b)
}

func(10) // NaN  doesn't work because 10 is assigned to a(first parameter) and b doesn't have a value.
func(20,30) // 50
```

Arrow function을 사용하는 가장 큰 이유는 this 때문이다. ES6에서 arrow function 을 사용하게 되면 자신을 감싸고 있는 곳을 this로 잡는다. 더 이상 function 밖에의 this를 사용하기 위해 주로 했던 const that = this; 라던지 bind 를 통해서 this를 전달(?) 할 필요가 없어진 것이다.
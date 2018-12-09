<h3>3. For of loops</h3>

for-of is a new loop in ES6 that replaces both for-in and forEach

for-of 는 ES6에서 새로 도입된 반복문이고 기존에 있던 for-in 과 forEach 를 대체한다.

```
forEach는 편리한 편이다.
let a = [1,2,3,4] 

a 배열을 돌면서 각 element 값을 알 수 있다.
a.forEach((item) => {
    console.info(item) 

    // 1
    // 2
    // 3
    // 4

})

하지만 forEach 는 배열에서 break 를 사용해서 나올 수 없다..

```



```

for (variable of iterable) {
    statement
}



```
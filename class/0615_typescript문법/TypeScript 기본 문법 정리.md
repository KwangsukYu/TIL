# TypeScript 기본 문법 정리

## 환경 설정

* 터미널

  ```bash
  npm install -g typescript
  ```

* React

  **이미 사용중인 프로젝트**

  ```typescript
  npm install --save typescript @types/node @types/react @types/react-dom @types/jest
  ```

  **새로운 프로젝트**

  ```typescript
  npx create-react-app my-app --template typescript
  ```

* Vue

  * 라이브러리 설치

  ```typescript
  vue add typescript
  ```

  * 사용

  ```vue
  <script lang="ts"> </script>
  ```

  

## 변수선언

**변수와 함께 타입을 선언한다**

* 타입의 종류 : string , number, boolean, bigint, null, undefined, [], {} ...
* 선언한 타입과 일치하지 않으면 오류

```typescript
// string
let name :string = 'kim'

name = 123; // JS에서는 가능하지만 TS에서는 오류

// array, object
let name :string[] = ['kim', 'park'] // string으로 되어있는 array
let age :{ age : number } = { age : 20 } //object
```

* 다양한 타입이 들어올 경우 | 기호를 이용해 or 연산자 표현

```typescript
let name :string | number = 'kim' //숫자 혹은 문자 할당 가능
```

* Template Literal Type
  * 새로운 타입을 만드는 도구 (변수와 구분하기위해 파스칼케이스로 작성)
  * Union Type 가능 (1:N, N:M 가능)
  * 자세한 활용은 추후 공부하기!

```typescript
type Toss = 'toss'

// type TossPayments = 'toss payments'
type TossPayments = `${Toss} payments`

type Companies = 'core' | 'banke' | 'securities' | 'payments' | 'insurance'
// type TossCompanies = 'toss core' | 'toss bank' | 'toss securities' | ...
type TossCompanies = `${Toss} ${Companies}`
```

* 함수

  * 함수는 파라미터와 return 값이 어떤 타입일지 지정가능

  ```typescript
  function func(x :nubmer) :number {
      return x * 2
  }
  ```

  * 단, 변수타입이 확실하지 않은 경우에는 마음대로 연산 불가능

  ```typescript
  // 에러, 변수 타입이 불확실
  function func(x :number | string) {
      return x * 2
  }
  
  // 가능
  function func(x :number | string) {
      if (typeof x === 'number'){
          return x * 2
      }
  }
  ```

* array 자료 안에 순서를 포함해 어떤 자료가 들어올지 정확히 지정하고 싶은 경우

```typescript
type Member = [number, boolean]
let john:Member = [100, false]
```

* object 타입 도 type 키워드로 변수 설정 가능
* interface 키워드 추후 공부

```typescript
type MyObject = {
    name : string,
    age : number
}

let johh :MyObject = {
    name : 'kim',
    age : 50
}

// 어떤 속성이 들어갈지 모를 땐 다 잡아서 넣어주기
type MyObject = {
    [key :string] : nmumber,
}
```

* class도 타입 설정이 가능하지만 해당 클래스의 프로퍼티는 미리 등록해두어야함

```typescript
class Person {
    name: string;
    constructor(name: string) {
        this.name = name;
    }
    
    walk() {
        console.log(`${this.name} is walking`);
    }
}
```






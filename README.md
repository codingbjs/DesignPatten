# Study Design Patten

### 1. Facade Patten
- 객체의 자율성 : 객체가 역할 및 책임을 수행하는 과정을 객체가 자율적으로 결정하도록 코드를 작성
- 관련 속성을 private 접근 제한으로 은익화 하고 수행에 관련된 속성만 public 접근 허용

### 2. Singleton Patten
- singleton.py : singleton 적용

### 3. OOP 적용
- CoffeeManager: OOP 미적용
- coffeemanager_oop : OOP 적용
- coffeemanager_oop_singleton : OOP 적용 - singleton
- coffeemanager_poly : 다형성 적용
 
### 4. Template Patten
- template : Template Patten : 외부 환경의 변화에 따라 변경되어야 하는 코드를 유연하게 외부로 위임하는 패턴
 
### 5. Strategy Patten
- strategy : Strategy Patten : 상속을 강제하지 않고 Template Patten 의 기능을 활용할 수 있는 설계 방식

### 6. Callback Patten
- template_callback : 기능 부분을 함수로 전달 받아 활용

### 7. Factory Patten
- factory : Factory Patten : Factory Class 에게 객체 생성을 위임하는 패턴

### 8. Builder Patten
- builder : Builder Patten : builder() 를 활용한 클래스 생성 - 가독성
- Calculator.py : 메서드 체인을 활용한 계산기 클래스

### 9. Proxy Patten
- proxy : Proxy Patten : 반복 사용되는 기능을 중복을 줄여 모듈화 하는 패턴

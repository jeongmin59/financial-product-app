# Django와 Vue.js를 활용한 금융 상품 비교 애플리케이션
### SSAFY 9기 1학기 관통 프로젝트
- 일시 : 2023.05.17(수) ~ 2023.05.26(금)

### 😎팀원 정보 및 업무 분담
| 이름 | 담당 영역 | Github |
| --- | ------ | ---------- |
| 공정민 | - 프론트엔드 / 백엔드 <br/> - Vue, 웹 디자인 정교화 등 | https://github.com/jeongmin59
| 김민구 | - 프론트엔드 / 백엔드 <br/> - django를 통한 DB 모델링 등 | https://github.com/kimingu7


### 📃Description
- 금융 상품 비교 및 추천 서비스 제공 프로젝트
- 기획 의도
    - 추후 수정 예정

### 🚩GOAL
- 금융 상품 데이터 기반 예적금 금리 비교 서비스 구성
- 금융 상품 추천 알고리즘 구성
- 환율 정보 API를 활용한 환율 계산 서비스 구성
- 지도 API를 활용한 은행 검색 서비스 구성
- 커뮤니티 서비스 구성
- 서비스 관리 및 유지 보수

### Tech Stack
- Django REST Framework & Vue2

### ERD (데이터 베이스 모델링)

### 컴포넌트 구조

### 서비스 플로우 차트

### 개발일지
| No |  Date |    Name   | ToDo |
| -- | ------- | ------------- | -------------- |
| 1 | 23/05/16 |  공정민  | 메인 페이지 동작 로직 구상 및 초기 CSS, 컴포넌트 구조 및 서비스 플로우 차트 마무리 |
| 2 | 23/05/16 |  김민구  | Google 및 Kakao API 활용해서 로그인 구현 시도 및 ERD 구축 |
| 3 | 23/05/17 |  공정민  | 메인 페이지 초기 CSS, 게시판 기능 구현 (일부) |
| 4 | 23/05/17 |  김민구  | dj_rest_auth를 활용한 자체 로그인 및 회원가입 기능 구현 </br> 게시판 CRUD 기능 및 Serializer 형태로 출력 확인 </br> 금융상품통합비교공시 API 호출 |
| 5 | 23/05/18 |  공정민  | 게시판 기능 구현, 로그인 및 회원가입 기능 구현 (일부) |
| 6 | 23/05/18 |  김민구  | 금융상품통합비교공시 API를 활용한 예,적금 상품 DB 저장 </br> 각 상품에 대한 상세 정보 출력 확인 </br> 카카오맵 API를 활용한 지도 일부 구현|
| 7 | 23/05/19 |  공정민  | 로그인 및 회원가입 연결 에러로 인한 대대적인 수정 </br> 처음부터 다시 짰으나 400 error 마주침 |
| 8 | 23/05/19 |  김민구  | 카카오맵 API을 활용하여 행정구역 근처 은행 검색 및 지도에 마커 표시 </br> 환율 API를 활용하여 주요 통화와 원화 사이의 환율 계산기 구현|
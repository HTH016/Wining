# Wining

### 개요

사용자 취향 기반 wine 추천 서비스 Wining입니다.<br>
스터디 프로젝트로 실제 서비스와는 관련이 없음을 밝힙니다.

#### 개발 일정
2023.07.10 ~ 2023.09.04

### (요구 사항)

***




### 기술 스택
- 언어 : <img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white"> <img src="https://img.shields.io/badge/html5-E34F26?style=for-the-badge&logo=html5&logoColor=white"> <img src="https://img.shields.io/badge/javascript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black">
- DB : <img src="https://img.shields.io/badge/mysql-4479A1?style=for-the-badge&logo=mysql&logoColor=white"> 
- Framework : <img src="https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=django&logoColor=white"> <img src="https://img.shields.io/badge/Vue.js-4FC08D?style=for-the-badge&logo=Vue.js&logoColor=black"/>
- Library : <img src="https://img.shields.io/badge/numpy-013243?style=for-the-badge&logo=numpy&logoColor=white"> <img src="https://img.shields.io/badge/pandas-150458?style=for-the-badge&logo=pandas&logoColor=white"> <img src="https://img.shields.io/badge/scikitlearn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=black"> <img src="https://img.shields.io/badge/jquery-0769AD?style=for-the-badge&logo=jquery&logoColor=white"> <img src="https://img.shields.io/badge/bootstrap-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white">
- 배포 : <img src="https://img.shields.io/badge/amazonec2-FF9900?style=for-the-badge&logo=amazonec2&logoColor=black"> <img src="https://img.shields.io/badge/gunicorn-499848?style=for-the-badge&logo=gunicorn&logoColor=white"> <img src="https://img.shields.io/badge/nginx-009639?style=for-the-badge&logo=nginx&logoColor=white">


***

### 아키텍쳐
<p align="center">
  <img src="https://github.com/user-attachments/assets/d3f01527-624a-4536-8073-cf720f365cce"  width="800" alt="description">
</p>

***

### 상세 기능

#### 검색
여러 가지 옵션을 선택하여 검색을 할 수 있습니다. 회원은 자동 추천 검색을 이용할 수 있습니다.
회원이 사전에 입력한 정보와, 판매 및 구매, 조회 이력을 수집하여 얻은 데이터로 협업필터링을 하여 
유사도가 높은 와인을 사용자가 선택한 갯수만큼 출력하도록 하였습니다.

<table>
  <tr>
    <td><img src="https://github.com/user-attachments/assets/ba710825-1baf-4695-bfea-aebcc2ad4d39" height="200" alt="Description 1"></td>
    <td>
      <img src="https://github.com/user-attachments/assets/876ca4c2-1443-4c51-a9ab-671c21481255" height="100" alt="Description 2"><br>
      <img src="https://github.com/user-attachments/assets/ff481e3a-b1ec-45b5-999b-45467f64531b" height="100" alt="Description 3">
    </td>
  </tr>
</table>
<img src="https://github.com/user-attachments/assets/7dc09463-80be-454d-a5c7-e3b266dec126" height="300" alt="description">


#### 판매 및 구매
주류는 배송이 법적으로 불가능하기 때문에 서비스에 등록한 판매자와 구매자가 수령코드를 대조할 수 있도록 구현했습니다.
수령코드는 base64를 이용하여 인코딩, 디코딩을 하도록 구현했습니다.

<img src="https://github.com/user-attachments/assets/843d4bd4-51f4-4f55-b839-b3c1947b8a32" height="250" alt="description"> <img src="https://github.com/user-attachments/assets/7aee1abf-32e5-4a7b-8794-97e4f94a719b" height="250" alt="description">

***

### 팀원 구성 및 역할
<table>
    <tr>
        <th style="width: 30%;">팀원</th>
        <th>역할 분담</th>
    </tr>
    <tr>
        <td>한태희</td>
        <td>Back-end, Front-end, MachineLearning <br>
        와인 검색, 회원 행동이력 데이터 생성, 와인 추천 모듈</td>
    </tr>
    <tr>
        <td>조범구</td>
        <td>Back-end, Front-end, 서버 배포 <br>
        매장 등록, 판매 구현, 구매 페이지, API 연동 적용, AWS 배포</td>
    </tr>
    <tr>
        <td>김민서</td>
        <td>Back-end, Front-end <br>
        게시판, 이미지 업로드, 웹UI/UX</td>
    </tr>
    <tr>
        <td>노지윤</td>
        <td>Back-end, Front-end, MachineLearning <br>
        회원 기능, 마이페이지, 리뷰 구현, 와인 추천 모듈</td>
    </tr>
</table>

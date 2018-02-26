# Parsing
* 이름 : Parsing
* 목적 : 스팸 url이 많이 노출돼 있는 사이트에서 노출돼 있는 모든 url을 파싱해 스팸 등록한다.
* 저자 : 김혜연
* 생성일 : 2015-12
* 개발 언어 : python
* python 버젼 : python 2.7
* 개발 환경 : Sublime Text3
* 저작권 : (c) kakao corp.

<사용된 외부 라이브러리>
* beautifulsoup4-4.5.0

<구현 프로세스>
* 해당 사이트의 html을 모두 파싱해 온 뒤, 필요한 url 외의 모든 태그를 제거하여 url만 출력한다.
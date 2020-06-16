PRIMARY KEY

해당 필드는 NOT NULL 과 UNIQUE 제약 조건의 특징을 모두 가집니다
이 제약조건이 설정된 필드는 NULL값을 가질 수 없으며 중복된 값도 가질 수 없습니다. 

1. NOT NULL(널값을 가지지 않을 것)
해당 필드는 NULL값을 저장할 수 없습니다. 이 제약조건이 설정된 필드는 무조건 데이터를 가지고 있어야 합니다.
예) KOR INT NOT NULL, 

2. UNIQUE(특별할 것)
해당 필드는 서로 다른 값을 가져야 합니다
즉, 중복된 값을 저장할 수 없습니다.
그렇지만 NULL 값을 허용합니다

예)

USERID VARCHAR(20) UNIQUE,

데이터가 아닌 것을 넘겨준다

그래서 NOT NULL을 붙여줍니다

그러면 중복되지 못하게 하고 NULL값 집어넣지 못하게 하면 PRIMARY KEY주면 되지 않느냐..

그런데 PRIMARY KEY 는 테이블당 1개만 집어넣을 수 있어서

UNIQUE 를 주면 된다. 

검색할때 빠르진 않는다

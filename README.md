#### with_datasets
- 공개 데이터셋 목록 
  - https://kbig.kr/portal/kbig/datacube.page
  - https://zdataset.com/

- 미지정(./codes)
  - randombynumpy.ipynb
  - seaborn_datasets.ipynb
  - sklearn_dataset.ipynb

|종류| 주제 | 주요 항목 |데이터| 작성 | 출처 | 참조 |
| :---: | --- | :---: | :---: | :---: | :---: | :---: |
| file| 주민등록인구통계| [cvs](https://jumin.mois.go.kr/index.jsp) | 주민등록인구통계,연령별 인구현황,주민등록 인구 기타현황 | encoding='cp949' | [행정안전부](https://mois.go.kr/) |  |
|file | 기상관측 | 지상,해양,고층,항공,세계기상전문 |[cvs](https://data.kma.go.kr/data/grnd/selectAsosRltmList.do?pgmNo=36)| 작성 | [기상자료개발포털](https://data.kma.go.kr) |  |
|file| 주택 실거래가 | 아파트 매매가 |[cvs](http://rtdown.molit.go.kr/)|[ipynb](./codes/주택실거래가.ipynb)| [국토교통부](http://rt.molit.go.kr/) | 참조 |
|api | COVID19 | summary, By Country Live |[APIs](https://documenter.getpostman.com/view/10808728/SzS8rjbc)| postman | [sourced from Johns Hopkins](https://covid19api.com/) | 참조 |
|file| 상권 정보 | 소상공인시장진흥공단_상가(상권)정보 |[cvs](https://www.data.go.kr/data/15083033/fileData.do)| [ipynb](./codes/전국상가분석.ipynb) | [공공데이터포털](https://www.data.go.kr/) | 참조 |
|file| 행동예측 | Breathing In-Depth, Wearables in the Wetlab |[uri](https://ubicomp.eti.uni-siegen.de/home/datasets/index.html.en?lang=en)| 작성 | 출처 | 참조 |

#### datasets
MNIST, CIFAR-10, CIFAR-100, STL-10, SVHN, Fashion MNIST

|분류| 제목 |데이터| 요구사항 | 작성 | 출처 | 참조 |
| :---: | --- | :---: | :---: | :---: | :---: | :---: |
|API| |openweathermap|[API](https://openweathermap.org/) | | 출처 | |
|Sample| sklearn datasets|| | [ipynb](./sklearn_dataset.ipynb) | 출처 | [api](https://scikit-learn.org/stable/datasets/toy_dataset.html) |
|Sample| seaborn datasets|| | [ipynb](./seaborn_datasets.ipynb) | 출처 | [api](https://seaborn.pydata.org/generated/seaborn.load_dataset.html) |
|Sample| AI hub|[AI hub](https://aihub.or.kr/)| 요구사항 | 분석 | 출처 | 참조 |
|회귀|[보스톤 집값 예측](./)|[sklearn](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_boston.html#sklearn.datasets.load_boston)|[kaggle](https://www.kaggle.com/c/gradient-boston-housing/data)|-|[git](https://github.com/bjpublic/MachineLearning/blob/master/06%EC%9E%A5_1%EC%A0%88_%EB%8D%B0%EC%9D%B4%ED%84%B0%EC%85%8B_%EC%84%A4%EB%AA%85.ipynb)||
|분류|[iris 꽃 예측](./)|[sklearn](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_boston.html#sklearn.datasets.load_iris)|-|-|[git](https://github.com/bjpublic/MachineLearning/blob/master/06%EC%9E%A5_1%EC%A0%88_%EB%8D%B0%EC%9D%B4%ED%84%B0%EC%85%8B_%EC%84%A4%EB%AA%85.ipynb)|-|
|분류|[와인 예측](./)|[sklearn](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_boston.html#sklearn.datasets.load_wine)|-|-|[git](https://github.com/bjpublic/MachineLearning/blob/master/06%EC%9E%A5_1%EC%A0%88_%EB%8D%B0%EC%9D%B4%ED%84%B0%EC%85%8B_%EC%84%A4%EB%AA%85.ipynb)|-|
|회귀|[당뇨병 예측](./)|[sklearn](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_boston.html#sklearn.datasets.load_diabetes)|-|-|[git](https://github.com/bjpublic/MachineLearning/blob/master/06%EC%9E%A5_1%EC%A0%88_%EB%8D%B0%EC%9D%B4%ED%84%B0%EC%85%8B_%EC%84%A4%EB%AA%85.ipynb)|-|
|회귀|[유방암 예측](./)|[sklearn](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_boston.html#sklearn.datasets.load_breast_cancer)|-|-|[git](https://github.com/bjpublic/MachineLearning/blob/master/06%EC%9E%A5_1%EC%A0%88_%EB%8D%B0%EC%9D%B4%ED%84%B0%EC%85%8B_%EC%84%A4%EB%AA%85.ipynb)|-|
|분류| Face Mask image|[kaggle](https://www.kaggle.com/datasets/ashishjangra27/face-mask-12k-images-dataset)|  |  |  |  |


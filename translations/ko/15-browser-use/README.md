# 컴퓨터 사용 에이전트(CUA) 구축

컴퓨터 사용 에이전트는 사람처럼 브라우저를 열고, 페이지를 검사하며, 화면에서 본 다음 최선의 행동을 취해 웹사이트와 상호작용할 수 있습니다. 이 수업에서는 Airbnb를 검색하고 구조화된 숙소 데이터를 추출하며 스톡홀름에서 가장 저렴한 숙박을 찾는 브라우저 자동화 에이전트를 구축합니다.

이 수업은 AI 기반 내비게이션을 위한 Browser-Use, 브라우저 제어를 위한 Playwright와 Chrome DevTools Protocol(CDP), 비전 기반 추론을 위한 Azure OpenAI, 그리고 구조화된 추출을 위한 Pydantic을 결합합니다.

## 소개

이 수업에서는 다음을 다룹니다:

- API 전용 자동화보다 컴퓨터 사용 에이전트가 적합한 경우 이해하기
- 신뢰할 수 있는 브라우저 라이프사이클 관리를 위해 Browser-Use와 Playwright 및 CDP 결합하기
- Azure OpenAI 비전과 구조화된 Pydantic 출력으로 동적 웹 페이지에서 숙소 데이터 추출하기
- 에이전트 우선, 액터 우선, 하이브리드 브라우저 자동화 워크플로 선택하기

## 학습 목표

이 수업을 완료하면 다음을 할 수 있습니다:

- Azure OpenAI와 Playwright로 Browser-Use 설정하기
- 실제 웹사이트를 탐색하고 동적 UI 요소를 처리하는 브라우저 자동화 워크플로 구축하기
- 페이지의 가시적 콘텐츠에서 타입화된 결과를 추출해 다운스트림 비즈니스 로직으로 변환하기
- 브라우저 작업 예측 가능성에 따라 에이전트와 액터 패턴 중 선택하기

## 코드 샘플

이 수업에는 하나의 노트북 튜토리얼이 포함되어 있습니다:

- [15-browser-user.ipynb](./15-browser-user.ipynb): CDP를 통해 Chrome 세션을 시작하고, Airbnb에서 스톡홀름 숙소 검색, Browser-Use 비전으로 가격 추출, 가장 저렴한 옵션을 구조화된 데이터로 반환합니다.

## 사전 준비 사항

- Python 3.12 이상
- 환경에 구성된 Azure OpenAI 배포
- 로컬에 설치된 Chrome 또는 Chromium
- 설치된 Playwright 종속성
- 비동기 Python 기본 지식

## 설정

노트북에서 사용하는 패키지를 설치하세요:

```bash
pip install browser_use playwright python-dotenv
playwright install chromium
```


노트북에서 사용하는 Azure OpenAI 환경 변수를 설정하세요:

```bash
AZURE_OPENAI_ENDPOINT=...
AZURE_OPENAI_API_KEY=...
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=...
# 선택 사항: 생략하면 최신 API 버전이 기본값입니다
AZURE_OPENAI_API_VERSION=...
```


## 아키텍처 개요

노트북은 하이브리드 브라우저 자동화 워크플로를 시연합니다:

1. Playwright와 Browser-Use가 동일한 브라우저 세션을 공유할 수 있도록 CDP가 활성화된 Chrome이 시작됩니다.
2. Browser-Use 에이전트가 Airbnb 열기, 팝업 닫기, 스톡홀름 검색 같은 개방형 내비게이션 작업을 처리합니다.
3. 활성 페이지를 구조화된 Pydantic 스키마로 검사해 숙소 제목, 1박 가격, 평점, URL을 추출합니다.
4. Python 로직이 추출된 목록을 비교하고 가장 저렴한 결과를 강조합니다.

이 접근법은 Browser-Use가 강점을 가진 유연한 비전 기반 추론을 유지하면서도 필요 시 결정론적인 브라우저 제어를 제공합니다.

## 주요 시사점 및 모범 사례

### 에이전트 vs 액터 사용 시기

| 시나리오 | 에이전트 사용 | 액터 사용 |
|----------|--------------|----------|
| 동적 레이아웃 | 예, AI가 페이지 변화를 적응 | 아니오, 깨지기 쉬운 선택자 |
| 알려진 구조 | 아니오, 에이전트가 직접 제어보다 느림 | 예, 빠르고 정확함 |
| 요소 찾기 | 예, 자연어가 잘 작동 | 아니오, 정확한 선택자 필요 |
| 타이밍 제어 | 아니오, 덜 예측 가능 | 예, 대기 및 재시도 완전 제어 |
| 복잡한 워크플로 | 예, 예기치 않은 UI 상태 처리 | 아니오, 명확한 분기 필요 |

### Browser-Use 모범 사례

1. 탐색과 동적 내비게이션에는 에이전트로 시작하세요.
2. 상호작용이 예측 가능해지면 직접 페이지 제어로 전환하세요.
3. 추출된 데이터가 검증되고 타입 안전하도록 구조화된 출력 모델 사용하세요.
4. 가시적 UI 변화를 일으키는 작업 뒤에는 지연을 전략적으로 추가하세요.
5. 반복 작업 중에는 스크린샷을 캡처해 실패 시 디버깅이 쉽도록 하세요.
6. 웹사이트 변경을 예상하고 팝업 및 레이아웃 변경에 대비한 대체 전략을 설계하세요.
7. 유연성과 정밀성을 동시에 얻기 위해 에이전트와 액터 패턴을 혼합하세요.

### 실제 활용 사례

- 여행 예약 및 가격 모니터링
- 전자상거래 가격 비교 및 재고 확인
- 동적 웹사이트에서의 구조화된 데이터 추출
- 비전 인식 UI 테스트 및 검증
- 웹사이트 모니터링 및 경고
- 다단계 플로우를 통한 지능형 양식 작성

## 추가 자료

- [Browser-Use Playwright 통합 템플릿](https://docs.browser-use.com/examples/templates/playwright-integration)
- [Browser-Use 액터 매개변수 및 콘텐츠 추출](https://docs.browser-use.com/customize/actor/all-parameters)
- [과정 설정](../00-course-setup/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 노력하였으나, 자동 번역에는 오류나 부정확성이 포함될 수 있음을 알려드립니다. 원문 문서는 해당 언어의 권위 있는 자료로 간주되어야 합니다. 중요한 정보의 경우, 전문 인간 번역을 권장합니다. 본 번역 사용으로 인한 오해 또는 오역에 대해 당사는 책임지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
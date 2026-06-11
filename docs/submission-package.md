<!-- STATUS: TEMPLATE -->

# Submission Package

## 1. 목적

본 문서는 Team Dandelion 1차 기본 프로젝트의 Google Drive 최종 제출 산출물 준비 상태를 관리하기 위한 문서이다.

GitHub Repository는 코드, 문서, 스크립트, 캡처의 원본 관리 공간으로 사용하고, Google Drive는 평가 제출용 최종 산출물 패키지 보관 공간으로 사용한다.

---

## 2. Google Drive 제출 폴더 구조

~~~text
Dandelion_1차_기본프로젝트/
├── 01_결과보고서/
│   ├── 결과보고서_Dandelion(Ansible기반_클라우드인프라자동화).pptx
│   └── 결과보고서_Dandelion(Ansible기반_클라우드인프라자동화).pdf
├── 02_시연영상/
│   └── 시연영상_Dandelion.mp4
├── 03_소스코드/
│   ├── dandelion-cloud-automation.zip
│   └── GitHub_URL.txt
├── 04_작업일지_회의록/
│   ├── 작업일지_Dandelion.md
│   └── 회의록_Dandelion.md
├── 05_구현결과_캡처/
│   ├── cloud-infra/
│   ├── server/
│   ├── ansible/
│   └── validation/
└── 06_기타자료/
    ├── README.md
    ├── project-status.md
    └── validation-summary.md
~~~

---

## 3. 최종 제출 산출물 체크리스트

| 구분 | 산출물 | 파일 형식 | 담당 | 상태 |
|---|---|---|---|---|
| 결과보고서 | 프로젝트 결과보고서 | PPTX | 정주헌 | 준비 중 |
| 결과보고서 | 프로젝트 결과보고서 | PDF | 정주헌 | 준비 중 |
| 시연 영상 | 기능별 시연 영상 | MP4 | 정주헌 / 전체 | 준비 중 |
| 소스 코드 | GitHub 최종 소스코드 압축본 | ZIP | 정주헌 | 준비 중 |
| 소스 코드 | GitHub Repository URL | TXT | 정주헌 | 준비 중 |
| 작업 일지 | 작업 일지 | MD 또는 DOCX | 정주헌 / 전체 | 준비 중 |
| 회의록 | 팀 회의록 | MD 또는 DOCX | 정주헌 / 전체 | 준비 중 |
| 구현 캡처 | 클라우드 인프라 캡처 | PNG | 백서빈 | 준비 중 |
| 구현 캡처 | 서버 / Docker 캡처 | PNG | 이진욱 | 준비 중 |
| 구현 캡처 | Ansible 실행 캡처 | PNG | 조민석 | 준비 중 |
| 구현 캡처 | 검증 / 백업 / 복구 캡처 | PNG | 박재우 | 준비 중 |
| 기타 자료 | README / project-status / validation-summary | MD 또는 PDF | 정주헌 | 준비 중 |
| 최종 제출 | Google Drive 업로드 완료 | Drive Folder | 정주헌 | 준비 중 |

---

## 4. 제출 완료 기준

아래 항목이 모두 준비되면 본 문서의 상태를 STATUS: COMPLETE로 변경한다.

~~~text
1. 결과보고서 PPTX 완료
2. 결과보고서 PDF 변환 완료
3. 시연 영상 MP4 완료
4. 소스코드 ZIP 생성 완료
5. GitHub URL 문서 작성 완료
6. 작업일지 / 회의록 정리 완료
7. 구현 결과 캡처 정리 완료
8. Google Drive 최종 폴더 업로드 완료
~~~

---

## 5. GitHub Repository

~~~text
https://github.com/snsd-hybirdinfra/dandelion-cloud-automation
~~~



---

## 6. 수시 업로드 운영 기준

Google Drive는 최종 제출용뿐 아니라 강사님 및 멘토님 확인을 위한 중간 산출물 공유 공간으로도 사용한다.

프로젝트 진행 중 아래 자료를 수시로 업로드한다.

| 구분 | 업로드 자료 | 업로드 시점 |
|---|---|---|
| 진행상태 | README.md / project-status.md / validation-summary.md | 주요 변경 발생 시 |
| 구현 캡처 | 인프라 / 서버 / Ansible / 검증 캡처 | 기능 구현 또는 검증 직후 |
| 멘토링 자료 | mentoring-brief / mentoring-questions | 멘토링 전 |
| 발표자료 | 결과보고서 PPT 초안 | 중간 점검 전 |
| 최종본 | PPTX / PDF / 영상 / ZIP / 작업일지 | 최종 제출 전 |

수시 업로드 자료와 최종 제출본은 구분하여 관리한다.

---

## 7. 수시 갱신 자료 기준

강사님 및 멘토님 확인을 위해 아래 자료는 프로젝트 진행 중 수시로 갱신하고 Google Drive에도 업로드한다.

| 구분 | 파일 | 목적 | 갱신 시점 |
|---|---|---|---|
| 프로젝트 요약 | README.md | 프로젝트 전체 개요 확인 | 주요 구조 변경 시 |
| 진행 상태 | docs/project-status.md | 담당자별 산출물 진행률 확인 | 팀원 push 후 |
| 자동 검수 | docs/validation-summary.md | 누락 파일 및 민감 파일 여부 확인 | 자동화 실행 후 |
| 제출 패키지 | docs/submission-package.md | Google Drive 제출 자료 준비 상태 확인 | 제출 자료 변경 시 |
| 회의록 | submission/meeting-notes.md | 회의 결정사항 및 역할 분담 확인 | 회의 후 |
| 작업일지 | submission/work-log.md | 날짜별 실제 작업 내역 확인 | 작업일 종료 전 |
| 발표자료 | presentation/presentation-outline.md | 결과보고서 및 발표 흐름 확인 | 발표 구성 변경 시 |

위 자료는 GitHub에 원본을 유지하고, Google Drive에는 강사님 및 멘토님 확인용으로 수시 업로드한다.

# 기계학습 환경 구성

Codebasic (c) 2015-2025

이 문서는 플랫폼별 기계학습 환경 설치 방법을 안내합니다. 아래 절차는 플랫폼 전반에 대체로 공통이며, 오픈소스 라이선스 소프트웨어만을 활용합니다.

## 플랫폼

1. 윈도우(Windows)
1. 유닉스 계열(Unix-like)
    1. 맥(macOS)
    1. 리눅스(Linux)

각 플랫폼별 환경 설정 섹션을 참조하여 설치를 진행할 수 있습니다.

## 콘다(Conda)

미니콘다(Miniconda)를 각 플랫폼별 안내에 따라 설치합니다.

[미니콘다(Miniconda) 설치](https://www.anaconda.com/docs/getting-started/miniconda/install)

콘다(Conda)는 크로스 플랫폼(cross-platform)에서 동작하며, 특정 언어에 종속되지 않는 범용 바이너리 패키지 관리자입니다.  

미니포지(Miniforge), 아나콘다 배포판(Anaconda Distribution)과 같은 콘다 배포판에서 사용되며, 다양한 시스템에서도 활용 가능합니다.  

주로 파이썬(Python) 기반 소프트웨어와 라이브러리 설치 및 환경 관리에 활용되지만, 다른 언어의 패키지와 도구도 관리할 수 있습니다.

콘다(Conda) 명령줄 인터페이스(CLI)는 전적으로 파이썬(Python)으로 작성되었으며, [BSD 라이선스](https://ko.wikipedia.org/wiki/BSD_%ED%97%88%EA%B0%80%EC%84%9C)의 오픈소스로 공개되어 있습니다. [Conda GitHub 저장소](https://github.com/conda/conda)

### 쉘 설정

콘다는 설치 후, 사용할 쉘에서 설정이 필요합니다.

```shell
conda init
```

#### 윈도우 파워셸(Windows PowerShell)

윈도우에서는 스크립트 실행 권한 설정이 필요할 수 있습니다.

```powershell
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

#### 설정 확인

모든 플랫폼에서 쉘을 재시작한 후 다음 명령으로 설정 확인:

```shell
conda --version
```

성공적으로 설정되면 버전 정보가 출력됩니다.

### 아나콘다(Anaconda)

- Anaconda, Inc.에서 배포하는 패키지 배포판  
- 파이썬, 콘다, 주요 과학계산/데이터분석 패키지(NumPy, pandas, scikit-learn 등) 기본 포함  
- 유의점:  
  - 기본 채널(defaults)은 상업적 사용 시 라이선스 제약 존재  

### 미니콘다(Miniconda)

- 최소 설치판: 파이썬 + 콘다만 포함  
- 필요한 패키지는 사용자가 직접 설치

### 콘다 채널 라이선스 비교(Conda channels)

#### 기본 채널(defaults, Anaconda)

- Anaconda, Inc.가 관리하는 기본 채널  
- 바이너리 배포본은 Anaconda 약관(Terms of Service) 적용  
- 상업적 사용(기업 환경) 시 별도 계약이 필요할 수 있음  

#### 콘다-포지(conda-forge)

- 전 세계 커뮤니티가 관리하는 채널  
- 패키지 본래의 오픈소스 라이선스 그대로 배포

## 소프트웨어 설치

상업적 사용 라이선스를 가정하지 않기 위해 아래 절차에서는 콘다-포지(conda-forge) 채널을 활용합니다.

### 파이썬 환경 생성

```shell
conda create --name pyml python=3.10 --channel conda-forge
```

#### 환경 활성화

생성된 환경 활성화:

```shell
conda activate pyml
```

성공하면 터미널 프롬프트에 `(pyml)` 표시가 나타납니다.

### 기계학습 라이브러리 구축

환경이 생성된 이후, 다음을 실행하여 소프트웨어 설치를 진행합니다.

```shell
conda install --name pyml --channel conda-forge scikit-learn pandas matplotlib ipykernel
```

### [선택적] 주피터 랩(Jupyter Lab)

[주피터 랩(Jupyter Lab)](https://jupyter.org/)은 웹 기반의 대화형 노트북 환경으로, 파이썬(Python) 코드 작성, 실행, 시각화를 한 곳에서 할 수 있습니다. 기계학습 실습에서 데이터 분석과 모델 개발에 주로 사용됩니다.

1. 커널 등록

    ```shell
    conda run --name pyml python -m ipykernel install --user --name pyml
    ```

1. 주피터 랩 설치

    ```shell
    conda install --name pyml --channel conda-forge jupyterlab
    ```

1. 주피터 랩 실행

    ```shell
    conda run --name pyml --no-capture-output jupyter-lab
    ```

실행하면 기본 웹 브라우저가 자동으로 열립니다.

터미널에서 주피터 서버(Jupyter Server) 주소를 확인하려면 다음 명령을 실행합니다.

```shell
conda run --name pyml jupyter server list
```

출력 예시:

```shell
Currently running servers:
http://localhost:8888/?token=82cd0... :: D:\pyml
```

## 도커(Docker)

도커를 활용하면 소프트웨어 설치와 설정이 완료된 상태로 바로 시작할 수 있습니다.

```shell
docker run --name pyml -d codebasic/pyml
```

### 주피터 서버(Jupyter Server)

컨테이너에서 주피터 서버(Jupyter Server)가 실행 중인 경우, 호스트 웹 브라우저에서 다음 주소로 접속합니다.

`http://localhost:8888`

토큰 값이 필요한 경우, 도커 컨테이너 쉘에서 다음 명령으로 토큰 값을 확인합니다.

```shell
docker exec pyml jupyter server list
```

컨테이너 내부의 URL은 호스트의 `localhost`로 접속해야 합니다. 다음 명령으로 호스트 주소로 치환할 수 있습니다.

- 파워쉘(Windows PowerShell)

```powershell
docker exec pyml jupyter server list | ForEach-Object { $_ -replace 'http://[^:]+', 'http://localhost' }
```

- POSIX 쉘 (bash/zsh 등)
  
```shell
docker exec pyml jupyter server list | sed -E 's#http://[^:]+#http://localhost#'
```

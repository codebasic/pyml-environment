Codebasic (c) 2023

다음 문서는 아래 플랫폼별 기계학습 소프트웨어 라이브러리 설치 절차를 안내합니다.

# 플랫폼

1. Windows (x86-64bit)
1. 유닉스 계열 (Unix-Like)
    1. Mac (Apple Silicon/Intel x86-64bit)
    1. Linux (x86-64bit)

제시된 절차는 오픈 소스 라이선스 소프트웨어만을 활용하고 있습니다. 제시된 절차는 오픈 소스 라이선스 소프트웨어만을 활용하고 있습니다. 
파이썬 환경 설정의 편의를 위해 Conda 소프트웨어를 활용합니다.

각 플랫폼별 환경 설정 섹션을 참조하여 설치를 진행할 수 있습니다.

## Windows

[Miniconda Windows](https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe) 다운로드 및 설치

설치 후, Anaconda Powershell Prompt에서 
[pyml.yml](pyml.yml) 파일을 참조하여 다음과 같이 설치를 진행합니다.

```powershell
conda env create -f pyml.yml
```

## Mac

애플 실리콘과 인텔(x86-64) 기반 모두 지원합니다.

아래 절차는 [Homebrew](https://brew.sh/index_ko) 소프트웨어를 가정합니다.

Conda 설치

```zsh
brew install miniconda
```

설치 완료 후, 쉘에서 conda 명령을 활용할 수 있도록 설정
```zsh
conda init "$(basename "${SHELL}")"
```

이후 절차는 **새 터미널**에서 진행합니다. 

### Apple Silicon

[apple_silicon.sh](apple_silicon.sh) 파일을 참조하여 다음과 같이 설치를 진행합니다.

```zsh
source ./apple_silicon.sh
```

### Intel CPU

[pyml.yml](pyml.yml) 파일을 참조하여 다음과 같이 설치를 진행합니다.

```zsh
conda env create -f pyml.yml
```

## Linux

[Miniforge](https://github.com/conda-forge/miniforge) 설치 스크립트 다운로드
```
wget -O Miniforge3.sh "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-$(uname)-$(uname -m).sh"
```

Miniforge 설치
```
./Miniforge3.sh
```

설치 완료 후, 쉘에서 conda 명령을 활용할 수 있도록 설정
```
conda init "$(basename "${SHELL}")"
```
이후 절차는 **새 터미널**에서 진행합니다. 

[pyml.yml](pyml.yml) 파일을 참조하여 다음과 같이 설치를 진행합니다.

```bash
conda env create -f pyml.yml
```

##  [선택적] Jupyter

코드 작성 환경 (IDE) Jupyter Lab 설치. [직접 설치](#직접-설치-native)를 진행한 경우를 가정합니다. 

도커 환경을 활용하는 경우는 설치와 설정이 완료되어 있습니다.

Jupyter Lab 설치

```bash
conda run -n pyml pip install jupyterlab
```

파이썬 환경을 주피터 커널로 등록합니다. 주의! 한글 사용자명. 예: C:\Users\성주

```bash
conda run -n pyml python -m ipykernel install --user --name pyml --display-name "pyml"
```

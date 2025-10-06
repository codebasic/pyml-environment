# 기계학습 환경 구성

Codebasic (c) 2015-2025

다음 문서는 아래 플랫폼별 기계학습 소프트웨어 라이브러리 설치 절차를 안내합니다.

제시된 절차는 오픈 소스 라이선스 소프트웨어만을 활용하고 있습니다. 제시된 절차는 오픈 소스 라이선스 소프트웨어만을 활용하고 있습니다. 파이썬 환경 설정의 편의를 위해 Conda 소프트웨어를 활용합니다.

## 플랫폼

1. Windows (x86-64bit)
1. 유닉스 계열 (Unix-Like)
    1. Mac (Apple Silicon/Intel x86-64bit)
    1. Linux (x86-64bit)

각 플랫폼별 환경 설정 섹션을 참조하여 설치를 진행할 수 있습니다.

## Conda

미니콘다를 각 플랫폼별 안내에 따라 설치합니다.

[Minconda 설치](https://www.anaconda.com/docs/getting-started/miniconda/install)

**Conda**는 크로스 플랫폼(cross-platform)에서 동작하며, 특정 언어에 종속되지 않는 범용 바이너리 패키지 관리자입니다.  
Miniforge, Anaconda Distribution과 같은 conda 배포판에서 사용되며, 다양한 시스템에서도 활용 가능합니다.  

주로 **파이썬 기반 소프트웨어와 라이브러리 설치 및 환경 관리**에 활용되지만, 다른 언어의 패키지와 도구도 관리할 수 있습니다.

**conda** 명령줄 인터페이스(CLI)는 전적으로 **Python**으로 작성되었으며, **BSD 라이선스의 오픈소스**로 공개되어 있습니다. [conda(GitHub)](https://github.com/conda/conda)

### Anaconda

- Anaconda, Inc.에서 배포하는 **풀 패키지 배포판**  
- Python, conda, 주요 과학계산/데이터분석 패키지(NumPy, pandas, scikit-learn 등) 기본 포함  
- 설치 직후 바로 데이터 분석/머신러닝 환경 활용 가능  
- 단점:  
  - 설치 용량이 큼.
  - 기본 채널(defaults)은 **상업적 사용 시 라이선스 제약** 존재  

### Miniconda

- **최소 설치판**: Python + conda만 포함  
- 필요한 패키지는 사용자가 직접 설치 (주로 conda-forge 활용)  
- 가볍고 유연 → 용량이 작고, 환경을 깨끗하게 유지 가능  
- 기업/기관 환경에서 **conda-forge 채널**과 함께 주로 사용  

### Conda 채널 라이선스 비교

#### defaults (Anaconda)

- Anaconda, Inc.가 관리하는 기본 채널  
- 패키지 본래의 오픈소스 라이선스는 동일  
- 단, **defaults 채널에서 제공하는 바이너리 배포본**은  
  Anaconda **Terms of Service** 적용  
- 상업적 사용(기업 환경) 시 별도 계약이 필요할 수 있음  

#### conda-forge

- 전 세계 커뮤니티가 관리하는 채널  
- 패키지 본래의 오픈소스 라이선스 그대로 배포  
- **추가적인 상업적 제약 없음**  
- 기업/개인 모두 자유롭게 사용 가능

## 소프트웨어 설치

Miniconda에서는 Anaconda 채널이 기본이기 때문에, 상업적 사용 라이선스를 가정하지 않기 위해 아래 절차에서는 conda-forge 채널을 활용합니다.

### 파이썬 환경 생성

```bash
conda create --name pyml python=3.10 -c conda-forge
```

### 기계학습 라이브러리 구축

환경이 생성된 이후, 다음을 실행하여 소프트웨어 설치를 진행합니다.

```bash
conda activate pyml
conda install -c conda-forge scikit-learn pandas matplotlib ipykernel
```

### [선택적] Jupyter

코드 작성 환경 (IDE) Jupyter Lab 설치

```bash
conda run --no-capture-output -n pyml conda install -c conda-forge jupyterlab
```

파이썬 환경을 주피터 커널로 등록합니다.

```bash
conda run --no-capture-output -n pyml python -m ipykernel install --user --name pyml --display-name "pyml"
```

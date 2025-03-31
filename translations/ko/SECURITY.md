<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0f93a8c33466486d1e7a0837ca8672ec",
  "translation_date": "2025-03-28T13:38:40+00:00",
  "source_file": "SECURITY.md",
  "language_code": "ko"
}
-->
# 보안

Microsoft는 자사 소프트웨어 제품과 서비스의 보안을 매우 중요하게 생각하며, 여기에는 [Microsoft](https://github.com/Microsoft), [Azure](https://github.com/Azure), [DotNet](https://github.com/dotnet), [AspNet](https://github.com/aspnet), [Xamarin](https://github.com/xamarin) 등의 GitHub 조직을 통해 관리되는 모든 소스 코드 저장소가 포함됩니다.

Microsoft가 정의한 [보안 취약점의 기준](https://aka.ms/security.md/definition)에 부합하는 Microsoft 소유의 저장소에서 보안 취약점을 발견했다고 생각되면, 아래 설명된 절차에 따라 보고해 주시기 바랍니다.

## 보안 문제 보고

**공개 GitHub 이슈를 통해 보안 취약점을 보고하지 마십시오.**

대신, Microsoft Security Response Center(MSRC)에 [https://msrc.microsoft.com/create-report](https://aka.ms/security.md/msrc/create-report)를 통해 보고해 주십시오.

로그인 없이 제출을 원하시면 [secure@microsoft.com](mailto:secure@microsoft.com)으로 이메일을 보내주세요. 가능하다면, 메시지를 Microsoft의 PGP 키로 암호화해 주세요. PGP 키는 [Microsoft Security Response Center PGP Key 페이지](https://aka.ms/security.md/msrc/pgp)에서 다운로드할 수 있습니다.

24시간 이내에 응답을 받을 수 있을 것입니다. 만약 응답이 없을 경우, 원래 메시지가 잘 전달되었는지 확인하기 위해 이메일로 후속 연락을 취해주시기 바랍니다. 추가 정보는 [microsoft.com/msrc](https://www.microsoft.com/msrc)에서 확인할 수 있습니다.

다음에 나열된 정보를 가능한 한 많이 포함하여 제공해 주시면 문제의 본질과 범위를 더 잘 이해할 수 있습니다:

* 문제 유형 (예: 버퍼 오버플로, SQL 인젝션, 크로스 사이트 스크립팅 등)
* 문제와 관련된 소스 파일의 전체 경로
* 영향을 받은 소스 코드의 위치 (태그/브랜치/커밋 또는 직접 URL)
* 문제를 재현하기 위해 필요한 특별한 구성
* 문제를 재현하기 위한 단계별 지침
* 개념 증명 또는 익스플로잇 코드 (가능한 경우)
* 문제의 영향, 특히 공격자가 문제를 어떻게 악용할 수 있는지

이 정보는 보고서를 더 빠르게 처리하는 데 도움이 됩니다.

버그 바운티를 위해 보고하는 경우, 더 완전한 보고서는 더 높은 바운티 보상으로 이어질 수 있습니다. 활성 프로그램에 대한 자세한 내용은 [Microsoft Bug Bounty Program](https://aka.ms/security.md/msrc/bounty) 페이지를 방문하십시오.

## 선호하는 언어

모든 커뮤니케이션은 영어로 진행되는 것을 선호합니다.

## 정책

Microsoft는 [Coordinated Vulnerability Disclosure](https://aka.ms/security.md/cvd) 원칙을 따릅니다.

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있지만, 자동 번역에는 오류나 부정확성이 있을 수 있습니다. 원본 문서(모국어로 작성된 문서)를 권위 있는 자료로 간주해야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.
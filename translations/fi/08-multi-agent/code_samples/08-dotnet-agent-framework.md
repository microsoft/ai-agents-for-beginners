# 🤝 Yrityksen moniedustajaisen työnkulkujärjestelmät (.NET)

## 📋 Oppimistavoitteet

Tämä muistikirja näyttää, kuinka rakentaa kehittyneitä yritystason moniedustajaisjärjestelmiä Microsoft Agent Frameworkin avulla .NET:ssä käyttäen Azure OpenAI:ta (Responses API). Opit orkestroimaan useita erikoistuneita edustajia työskentelemään yhdessä rakenteellisten työnkulkujen kautta, hyödyntäen .NET:n yritysominaisuuksia tuotantovalmiisiin ratkaisuihin.

**Rakennettavia yrityksen moniedustajaisominaisuuksia:**
- 👥 **Edustajien yhteistyö**: Tyyppiturvallinen edustajien koordinointi käännösaikaisen validoinnin kera
- 🔄 **Työnkulun orkestrointi**: Deklaratiivinen työnkulun määrittely .NET:n asynkronisten mallien avulla
- 🎭 **Roolien erikoistuminen**: Vahvasti tyypitetyt edustajien persoonallisuudet ja asiantuntija-alueet
- 🏢 **Yrityksen integrointi**: Tuotantovalmiit mallit valvonnalla ja virheiden käsittelyllä

## ⚙️ Vaatimukset ja käyttöönotto

**Kehitysympäristö:**
- .NET 9.0 SDK tai uudempi
- Visual Studio 2022 tai VS Code C#-laajennuksella
- Azure-tilaus (jatkuville edustajille)

**Vaaditut NuGet-paketit:**
```xml
<PackageReference Include="Microsoft.Extensions.AI.Abstractions" Version="10.*" />
<PackageReference Include="Azure.AI.Agents.Persistent" Version="1.2.0-beta.10" />
<PackageReference Include="Azure.Identity" Version="1.15.0" />
<PackageReference Include="System.Linq.Async" Version="6.0.3" />
<PackageReference Include="Microsoft.Extensions.AI" Version="10.*" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
<PackageReference Include="Microsoft.Extensions.AI.OpenAI" Version="10.*" />
<PackageReference Include="OpenTelemetry.Api" Version="1.*" />
<PackageReference Include="Microsoft.Agents.AI.Workflows" Version="1.*" />
<PackageReference Include="Microsoft.Agents.AI.OpenAI" Version="1.*-*" />
```

## Koodiesimerkki

Tämän oppitunnin täydellinen toimiva koodi löytyy mukanaolevasta C#-tiedostosta: [`08-dotnet-agent-framework.cs`](../../../../08-multi-agent/code_samples/08-dotnet-agent-framework.cs)

Esimerkin suorittamiseksi:

```bash
# Tee tiedostosta suoritettava (Linux/macOS)
chmod +x 08-dotnet-agent-framework.cs

# Suorita esimerkki
./08-dotnet-agent-framework.cs
```

Tai .NET CLI:llä:

```bash
dotnet run 08-dotnet-agent-framework.cs
```

## Mitä tämä esimerkki havainnollistaa

Tämä moniedustajainen työnkulkujärjestelmä luo hotelli- ja matkasuosituspalvelun kahdella erikoistuneella edustajalla:

1. **FrontDesk-edustaja**: Matkatoimisto, joka tarjoaa aktiviteetti- ja sijaintisuosituksia
2. **Concierge-edustaja**: Tarkistaa suositukset varmistaakseen aidot, ei-turistiset kokemukset

Edustajat toimivat yhdessä työnkulussa, jossa:
- FrontDesk-edustaja vastaanottaa alkuperäisen matkatoiveen
- Concierge-edustaja tarkistaa ja hiottaa suosituksia
- Työnkulku striimaa vastaukset reaaliajassa

## Keskeiset käsitteet

### Edustajien koordinointi
Esimerkki näyttää tyyppiturvallisen edustajien koordinoinnin Microsoft Agent Frameworkin avulla käännösaikaisella validoinnilla.

### Työnkulun orkestrointi
Käyttää deklaratiivista työnkulun määrittelyä .NET:n asynkronisten mallien avulla yhdistääkseen useita edustajia putkeen.

### Vastauksien striimaus
Toteuttaa reaaliaikaisen vastausten striimauksen edustajilta asynkronisten enumeratiivien ja tapahtumapohjaisen arkkitehtuurin avulla.

### Yrityksen integrointi
Näyttää tuotantovalmiita malleja, mukaan lukien:
- Ympäristömuuttujien konfigurointi
- Turvallinen tunnistetietojen hallinta
- Virheiden käsittely
- Asynkroninen tapahtumien käsittely

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
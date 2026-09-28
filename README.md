<!-- # Saklob (SKLB) -->

<p align="center">
    <img src="saklob.svg"
        height="42"
        alt="Saklob sa Baybayin"
        style="vertical-align: middle;">
</p>

<p align="center">
    <strong>Pagtatangkang gumawa ng maliit at disenteng kaligirang pang-utos.</strong>
</p>

## Talaan ng Nilalaman

- [Ano ang Saklob](#ano-ang-saklob)
- [Bakit Saklob](#bakit-saklob)
- [Disenyo at Pilosopiya](#disenyo-at-pilosopiya)
- [Unang Target: Arduino Nano ESP32](#unang-target-arduino-nano-esp32)
- [LNDH: Unang Application](#lndh-unang-application)
- [Hindi Lang Tungkol sa Wika](#hindi-lang-tungkol-sa-wika)
- [Mga Core na Bahagi](#mga-core-na-bahagi)
- [Roadmap: Python → C++ → Embedded](#roadmap-python--c-embedded)
- [Context at Prompt](#context-at-prompt)
- [Ano ang Hindi Saklob](#ano-ang-hindi-saklob)
- [Project Status](#project-status)
- [Sa Madaling Salita](#sa-madaling-salita)

---

## Ano ang Saklob

Ang Saklob (SKLB) ay isang personal at eksperimental na command environment na ginagawa para sa maliliit at naka-embed na sistema.

Nagsimula ito sa isang simpleng tanong:

> Paano kung gumawa ng sariling command-line environment na sapat lang ang features para maging useful, pero hindi kailangang maging sobrang laki at komplikado?

Hindi goal ang gumawa ng bagong PowerShell o Bash — may mga tool na para doon, at hindi rin practical na subukang tapatan sila. Mas interesante ang gumawa ng maliit na command environment na tumatakbo sa mga system na limitado ang resources, lalo na sa Arduino Nano ESP32.

## Bakit Saklob

Sa desktop, sanay tayo sa command environment na may napakaraming capability — filesystem, processes, environment variables, scripting, package ecosystem, networking, atbp.

Sa microcontroller, iba ang usapan: mas limitado ang memory, storage, at processing time. Kaya hindi dinadala nang buo ang desktop-style shell papunta sa isang microcontroller.

Ang minimal na modelo:

```
input → parser → command → handler → system/module → output
```

Iyon lang muna. Kung hindi kailangan ang isang feature para gumana nang maayos ang command environment, hindi ito idinadagdag agad. Mas interesante kung gaano kaliit ang puwedeng maging command environment habang useful pa rin ito.

## Disenyo at Pilosopiya

Ayaw gawing "feature monster" ang Saklob. Kung ganito na ang itsura:

```
Saklob
 ├── parser
 ├── scripting language
 ├── package manager
 ├── process manager
 ├── networking stack
 ├── filesystem
 ├── GUI
 ├── ...
 └── 500 dependencies
```

...talo na ang orihinal na idea. Mas gusto ang maliit pero maayos:

```
Saklob
 ├── command
 ├── parser
 ├── context
 ├── registry
 ├── module
 ├── session
 └── output
```

Kung may idadagdag, dapat may malinaw na dahilan kung bakit.

## Unang Target: Arduino Nano ESP32

Hindi kailangang tumakbo agad ang buong Saklob dito. Sa ngayon, Python muna ang implementation dahil mas mabilis mag-experiment doon — mas madaling subukan ang parser, command registry, context, prompt, modules, errors, at iba pang behavior bago isipin kung paano ito gagawing maliit na C++ implementation.

```
Python → experiment → find what actually matters → simplify → C++ → Arduino Nano ESP32
```

Hindi rin plano na i-port nang literal ang Python code papuntang C++ — hindi naman kailangang ganon. Ang Python implementation ay parang laboratoryo: dito malalaman kung ano talaga ang kailangan bago gawin ang mas maliit na implementation para sa embedded side.

## LNDH: Unang Application

Ang LundayHangin (LNDH) ang unang application ng Saklob. Kailangan dito ng paraan para makapag-interact sa iba't ibang subsystem nang hindi gumagawa ng hiwalay na interface para sa bawat isa — dito pumapasok ang Saklob.

Halimbawa ng mga command:

```
show system
show gnss
show motor
show power
show communications
show attitude
```

Hindi ibig sabihin na ang GNSS, motor, power, atbp. ay bahagi mismo ng Saklob. Ang Saklob ang nagbibigay ng command environment; ang LNDH ang may actual na functionality:

```
              Saklob
                 │
          command environment
                 │
        ┌────────┼────────┐
        │        │        │
       GNSS     Motor    Power
        │        │        │
        └────────┼────────┘
                 │
                LNDH
```

Layunin na manatiling ganito ang separation hangga't maaari. Kung may ibang proyekto balang araw na gustong gumamit ng Saklob, hindi na ito kailangang maging LNDH project.

## Hindi Lang Tungkol sa Wika

Isa sa mga eksperimento sa Saklob ay ang paggamit ng iba't ibang wika sa command interface — halimbawa, `show status` at ang katumbas nito sa ibang command vocabulary (Filipino, posibleng Cebuano, o iba pang wika).

Pero hindi ito ang buong point ng Saklob — localization ay isang bahagi lang ng project. Mas mahalaga ang paghihiwalay ng command na naiintindihan ng user mula sa internal representation na naiintindihan ng program.

Kung `ipakita kalagayan` at `show status` ay parehong tumutukoy sa isang internal command, hindi kailangang magbago ang actual command handler kahit nagbago ang wikang ginamit. Sa ganitong paraan, nagiging user-facing lang ang wika nang hindi nito kailangang guluhin ang core.

## Mga Core na Bahagi

Sa Python implementation, sinusuri ang mga sumusunod:

- command parsing
- command registration
- command execution
- context
- prompt
- session
- modules
- errors
- localization

Hindi lahat ng ito ay kailangang mapunta sa final embedded implementation — isa sa goals ng Python version ay malaman kung ano ang puwedeng tanggalin.

Mental model sa ngayon:

```
User
 │
 ▼
Input → Parser → Command/Context → Command Registry → Handler → Module/Host → Output
```

Hindi pa ito final na architecture. Puwedeng magbago ang mga pangalan, layers, o boundaries habang mas naiintindihan kung ano talaga ang kailangan.

## Roadmap: Python → C++ → Embedded

```
SKLB Python
    │
    ├── experiment
    ├── test ideas
    ├── develop command model
    └── find the minimum useful design
                │
                ▼
           SKLB C++
                │
                ▼
       Arduino Nano ESP32
                │
                ▼
              LNDH
```

Kapag sapat na ang natutunan mula sa Python implementation, susunod ang C++, kung saan mas seryoso ang consideration sa:

- memory usage
- static / compile-time resources
- dynamic allocation
- execution time
- serial I/O
- code size

Target muna ang Arduino Nano ESP32, pero ayaw gawing sobrang Nano-specific ang core kung hindi naman kailangan. Kung maayos ang abstraction, baka puwede itong gamitin sa iba pang microcontroller o embedded platform.

Hindi kailangang madaliin ang pagpunta sa C++ — mas mahalagang malinaw muna kung ano talaga ang Saklob.

## Context at Prompt

Eksperimento rin ang pagkakaroon ng context sa command environment. Halimbawa:

```
salig@lndh(dron)>
salig@lndh(dron)(motor)>
```

Hindi pa kailangang maging sobrang sophisticated nito. Ang layunin muna ay magkaroon ng malinaw na paraan para malaman ng Saklob kung nasaan ang user sa command environment at kung anong commands ang relevant sa kasalukuyang context.

Kasama rin dito ang mga naunang ideya tungkol sa identity at roles:

- `salig`
- `bahala`
- `malim`
- `balana`

Habang experimental pa ang project, hindi pa itinuturing na final ang mga ito.

## Ano ang Hindi Saklob

- Hindi kapalit ng PowerShell
- Hindi kapalit ng Bash
- Hindi operating system
- Hindi RTOS
- Hindi full scripting language
- Hindi LNDH mismo
- Hindi malaking framework na kailangang gamitin ng lahat

Kung may existing tool na mas magandang gamitin para sa isang problema, okay lang gamitin iyon. Ang Saklob ay primarily isang experiment sa paggawa ng maliit na command environment.

## Project Status

**Experimental / early development**

- Python muna ang pangunahing implementation
- Hindi pa stable ang API, command syntax, architecture, o package structure
- Normal lang na may mga bagay na mapalitan o matanggal habang ginagawa ang project

Mas gusto ang pag-discover ng tamang design kaysa mag-decide agad ng malaking architecture tapos piliting sundin iyon kahit hindi naman kailangan.

## Sa Madaling Salita

Ang Saklob ay isang personal na pagtatangka na gumawa ng maliit pero disenteng command environment. Hindi goal ang gumawa ng pinakamalaking shell, pinakamaraming feature, o bagong replacement para sa existing tools.

Ang gusto malaman:

> Puwede kayang gumawa ng command environment na simple at magaan enough para sa isang Arduino Nano ESP32, pero hindi naman sobrang barebones na wala nang silbi?

LNDH ang unang application kung saan ito susubukan. Python muna ang laboratoryo, C++ ang susunod na hakbang. At kung maayos ang lahat, doon malalaman kung may tunay na silbi ang Saklob sa isang maliit na embedded system.
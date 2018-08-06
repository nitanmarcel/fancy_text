# Instalation:

Stable from pip:
 ```
pip install fancy_text
```

From development branch [beta]
```
git pull https://github.com/nitanmarcel/fancy_text -b development

pip install -e fancy_text/

```

# Usage:

 ```
>>> from fancy_text import fancy

>>> text = 'This is so fancy'

>>> print(fancy.light(text))
𝔗𝔥𝔦𝔰 𝔦𝔰 𝔰𝔬 𝔣𝔞𝔫𝔠𝔶

>>> print(fancy.bold(text))
𝕿𝖍𝖎𝖘 𝖎𝖘 𝖘𝖔 𝖋𝖆𝖓𝖈𝖞

>>> print(fancy.box(text))
🆃🅷🅸🆂 🅸🆂 🆂🅾 🅵🅰🅽🅲🆈
```


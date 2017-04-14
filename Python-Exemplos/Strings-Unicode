>>> # Strings Unicode

>>> # A partir de Python 2.0 um novo tipo foi introduzido: o objeto Unicode. Ele pode ser usado para armazenar e manipular
>>> # dados Unicode (veja http://www.unicode.org/) e se integra bem aos demais objetos strings pré-existentes, de forma a
>>> # realizar auto-conversões quando necessário.

>>> # Unicode tem a vantagem de prover um único número ordinal para cada caracter usado em textos modernos ou antigos. 
>>> # Previamente, havia somente 256 números ordinais. Logo, mapeamentos entre conjuntos de caracteres e os 256 números 
>>> # ordinais precisavam ser indexados por códigos de página. Isso levou a uma enorme confusão especialmente no âmbito 
>>> # da internacionalização (tipicamente escrito como "i18n" - "i" + 18 caracteres + "n") de software. 
>>> # Unicode resolve esses problemas ao definir um único código de página para todos os conjuntos de caracteres.

>>> # Criar strings Unicode em Python é tão simples quanto criar strings normais:

>>> u'Hello World !'
u'Hello World !'

>>> # O pequeno "u" antes das aspas indica a criação de uma string Unicode . Se você desejar incluir caracteres especiais
>>> # na string, você pode fazê-lo através da codificação Python Unicode-Escape.

>>> u'Hello\u0020World !'
u'Hello World !'

>>> # O código de escape \u0020 indica a inserção do caracter Unicode com valor ordinal 0x0020 (o espaço em branco) na
>>> # posição determinada.

>>> # Os outros caracteres são interpretados através de seus respectivos valores ordinais diretamente para os valores 
>>> # ordinais em Unicode. Se você possui strings literais na codificação padrão Latin-1 que é utilizada na maioria do
>>> # oeste europeu, você achará conveniente que os 256 caracteres inferiores do Unicode coincidem com os 256 caracteres
>>> # inferiores do Latin-1.

>>> # Para experts, existe ainda um modo cru (N.d.T: sem processamento de caracteres escape) da mesma forma que existe
>>> # para strings normais. Basta prefixar a string com 'ur' para utilizar a codificação Python Raw-Unicode-Escape. 
>>> # Só será aplicado a conversão \ uXXXX se houver um número ímpar de barras invertidas antes do escape 'u'.

>>> ur'Hello\u0020World !'
u'Hello World !'
>>> ur'Hello\\u0020World !'
u'Hello\\\\u0020World !'

>>> # O modo cru (N.d.T: raw) é muito útil para evitar excesso de barras invertidas, por exemplo, em expressões regulares.

>>> # Além dessas codificações padrão, Python oferece um outro conjunto de maneiras de se criar strings Unicode sobre uma
>>> # codificação padrão.

>>> # A função interna unicode() provê acesso a todos os Unicode codecs registrados (COders and DECoders).

>>> # Alguns dos mais conhecidos codecs são : Latin-1, ASCII, UTF-8, and UTF-16. Os dois últimos são codificações de tamanho
>>> # variável para armazenar cada caracter Unicode em um ou mais bytes. A codificação default é ASCII, que trata normalmente
>>> # caracteres no intervalo de 0 a 127 mas rejeita qualquer outro com um erro. Quando uma string Unicode é impressa, escrita
>>> # em arquivo ou convertida por str(), a codificação padrão é utilizada.

>>> u"abc"
u'abc'
>>> str(u"abc")
'abc'
>>> u"äöü"
u'\xe4\xf6\xfc'
>>> str(u"äöü")
Traceback (most recent call last):
  File "<stdin>", line 1, in ?
UnicodeEncodeError: 'ascii' codec can't encode characters in position
0-2: ordinal not in range(128)

>>> # Para se converter uma string Unicode em uma string 8-bits usando uma codificação específica, basta invocar o método
>>> # encode() de objetos Unicode passando como parâmetro o nome da codificação destino. É preferível utilizar nomes de
>>> # codificação em letras minúsculas.

>>> u"äöü".encode('utf-8')
'\xc3\xa4\xc3\xb6\xc3\xbc'

>>> # Também pode ser utilizada a função unicode() para efetuar a converção de um string em outra codificação. Neste caso,
>>> # o primeiro parâmetro é a string a ser convertida e o segundo o nome da codificação almejada. O valor de retorno da 
>>> # função é a string na nova codificação.

>>> unicode('\xc3\xa4\xc3\xb6\xc3\xbc', 'utf-8')
u'\xe4\xf6\xfc'

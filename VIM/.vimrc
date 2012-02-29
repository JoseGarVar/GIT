
" FUNCIONAMIENTO GENERAL
￼set helplang=es

" VISUALIZACIÓN
set ruler
set showmode
set showcmd
syntax enable  " Coloreado de sintaxis
set showmatch  " Cuando se cierran paréntesis, llaves o corchetes
               " muestra con qué carácter coinciden.


" SANGRADO, SALTOS DE LÍNEA Y TABULADORES

" BÚSQUEDAS
set hlsearch   " Iluminar todas las apariciones de la cadena
               " buscada


" COMANDOS PROPIOS Y ABREVIATURAS
:set number

autocmd VimEnter * NERDTree
autocmd VimEnter * wincmd p

map <F2> :NERDTreeToggle<CR>

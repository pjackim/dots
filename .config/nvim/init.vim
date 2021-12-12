let g:vim_markdown_folding_disabled = 1
let g:NERDTreeDirArrowExpandable = ''
let g:NERDTreeDirArrowCollapsible = ''

" BASIC
set directory^=$XDG_CACHE_HOME/vim//
set autoindent
set expandtab
set smarttab
set tabstop=4
set shiftround
set shiftwidth=4
set wildmode=longest,list,full
set hlsearch
set ignorecase
set smartcase

" SHORCUTS
let mapleader=" "

map <C-g> :Goyo<CR> 
map <C-c> :ColorToggle<CR>
map <C-n> :NERDTreeToggle<CR>
map <C-w> :WP<CR>
map <C-x> :%s//gI<Left><Left><Left>
map <C-s> :setlocal spell spelllang=en_us<CR>

" BASIC AUTOCMD
autocmd BufRead,BufNewFile ~/usr/notes set filetype=markdown

" INTERFACE
set laststatus=2
set noruler
set noshowcmd
set number relativenumber
set noerrorbells
set visualbell
set mouse=a
set splitbelow splitright

" COLOR
"set termguicolors
" colorscheme cs

" RENDERING
set encoding=utf-8
set linebreak
syntax enable

" MISC
set backspace=indent,eol,start
set history=10000

" CUSTOM FUNCTIONS

" Run xrdb whenever Xdefaults or Xresources are updated.
" Also run replace command for changing config files which cannot use
" Xresources directly
autocmd BufWritePost *Xresources,*Xdefaults !xrdb %; xrdb-replace -F -g 

" Search function for notes directory
command! -nargs=1 Ngrep vimgrep "<args>" $NOTES_DIR/**/*.txt

" Open NERDTree if opening a directory
autocmd StdinReadPre * let s:std_in=1
autocmd VimEnter * if argc() == 1 && isdirectory(argv()[0]) && !exists("s:std_in") | exe 'NERDTree' argv()[0] | wincmd p | ene | exe 'cd '.argv()[0] | endif

" Prose editing function
func! WordProcessor()
  " movement changes
  map j gj
  map k gk
  " formatting text
  setlocal formatoptions=1
  setlocal noexpandtab
  setlocal wrap
  setlocal linebreak
  " spelling and thesaurus
  setlocal spell spelllang=sv
  " set thesaurus+=/home/test/.vim/thesaurus/mthesaur.txt
  " complete+=s makes autocompletion search the thesaurus
  set complete+=sterrain
endfu
com! WP call WordProcessor()

" This line makes pacman-installed global Arch Linux vim packages work.
" require("telescope").setup()
source /usr/share/nvim/archlinux.vim
syntax on

" set number
" od primegeagena   

set relativenumber
set nonumber
set guicursor=
set nohlsearch
set noerrorbells
set tabstop=4 softtabstop=4
set shiftwidth=4 
set expandtab 
set smartindent 
set nu
" set nowrap
set wrap
set smartcase
set noswapfile
set incsearch
set hidden
"se mouse+=a

"call plug#begin(~/.local/share/nvim/site/autoload)    
" call plug#begin(stdpath('data').'/site/autoload/plugged')    
call plug#begin('/etc/xdg/nvim/autoload')
" call plug#begin()    
 Plug 'arcticicestudio/nord-vim'
 Plug 'Mofiqul/dracula.nvim'
 Plug 'ambv/black'
 Plug 'gruvbox-community/gruvbox'
 Plug 'nvim-treesitter/nvim-treesitter', {'do': ':TSUpdate'}  " We recommend updating the parsers on update
"plug 'jremmen/vim-ripgrep'    
"plug 'tpope/vim-fugitive'    
"plug 'git@github.com:Valloric/YourCompleteMe.git'    
 Plug 'neovim/nvim-lspconfig'   
 Plug 'fatih/vim-go', { 'do': ':GoUpdateBinaries' }
 "Plug 'fatih/vim-go'
 Plug 'itchyny/lightline.vim'
 Plug 'ap/vim-css-color'
 Plug 'nvim-lua/plenary.nvim'
 Plug 'nvim-telescope/telescope.nvim'
call plug#end()

"colorscheme nord
"colorscheme peachpuff
colorscheme dracula
highlight Normal guibg=none
autocmd BufRead,BufNewFile /tmp/calcurse* set filetype=markdown
autocmd BufRead,BufNewFile ~/.calcurse/nites/* set filetype=markdown


let g:go_bin_path = $HOME."/go/bin"
"let g:go_bin_path = $HOME."/go/bin"



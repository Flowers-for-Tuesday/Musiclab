\version "2.24.2"

\paper {
  #(define output-format 'svg) % 可改为 pdf
  indent = 0\mm                % 不缩进
  line-width = 100\mm          % 控制乐谱长度
  ragged-right = ##t           % 不强制右对齐
  tagline = ##f                % 不显示右下角标签
  top-margin = 0\mm
  bottom-margin = 0\mm
  left-margin = 0\mm
  right-margin = 0\mm
  
}

\layout {
  \context {
    \Score
    \remove "Bar_number_engraver"
  }
}

\score {
  \relative c' {
    \key c \major
    \time 4/4
    c4 d e f g a b c
  }
}

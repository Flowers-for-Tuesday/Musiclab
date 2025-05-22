\version "2.24.2"

\paper {
  #(define output-format 'svg)   % 输出为SVG，可改为 pdf
  indent = 0\mm                  % 不缩进
  line-width = 100\mm            % 一行乐谱长度
  ragged-right = ##t             % 不强制对齐右边
  tagline = ##f                  % 不显示底部 LilyPond 标记
  top-margin = 0\mm
  bottom-margin = 0\mm
  left-margin = 0\mm
  right-margin = 0\mm
  system-system-spacing = #'((basic-distance . 0) (minimum-distance . 0) (padding . 0) (stretchability . 0))
  page-breaking = #ly:one-page-breaking
}

\layout {
  \context {
    \Score
    \remove "Bar_number_engraver"  % 不显示小节编号
  }
}


\score {
  <<
    \new Staff {
      \relative c' { c4 d e f | g a b c | }
    }
    \new Staff {
      \clef bass
      \relative c { c4 b a g | f e d c | }
    }
  >>
}

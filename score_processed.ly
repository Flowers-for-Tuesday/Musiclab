\version "2.24.4"
% automatically converted by musicxml2ly from score.musicxml
\pointAndClickOff


#(set-global-staff-size 20.0)
\paper {
    
    }
\layout {
    \context { \Score
        autoBeaming = ##f
        }
    }
PartPOneThreedFivebOnebaEightaSixSevenThreecfeOneaSixEightFiveadNineThreedcZerodfSixNineVoiceOne = 
\relative c'' {
    \clef "treble" \numericTimeSignature\time 4/4 \key c \major | % 1
    \tempo 4=90 c4 e4 f4 g4 | % 2
    r4 -. a2 s2*5 \bar "|."
    }

PartPSevenbSevenFivebaSevenNineeEightebeTwobZerobbaEighteOneSevenFiveecThreeaddTwoSevenVoiceOne = 
\relative c {
    \clef "bass" \numericTimeSignature\time 4/4 \key c \major | % 1
    <c e g>2 <f a c>2 | % 2
    <g b d>2 r4 c,4 | % 3
    <a e'>2 s4*7 \bar "|."
    }


% The score definition
\score {
    <<
        
        \new Staff
        <<
            \set Staff.instrumentName = "Soprano"
            \set Staff.shortInstrumentName = "S"
            
            \context Staff << 
                \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                \context Voice = "PartPOneThreedFivebOnebaEightaSixSevenThreecfeOneaSixEightFiveadNineThreedcZerodfSixNineVoiceOne" {  \PartPOneThreedFivebOnebaEightaSixSevenThreecfeOneaSixEightFiveadNineThreedcZerodfSixNineVoiceOne }
                >>
            >>
        \new Staff
        <<
            \set Staff.instrumentName = "Bass"
            \set Staff.shortInstrumentName = "B"
            
            \context Staff << 
                \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                \context Voice = "PartPSevenbSevenFivebaSevenNineeEightebeTwobZerobbaEighteOneSevenFiveecThreeaddTwoSevenVoiceOne" {  \PartPSevenbSevenFivebaSevenNineeEightebeTwobZerobbaEighteOneSevenFiveecThreeaddTwoSevenVoiceOne }
                >>
            >>
        
        >>
    \layout {}
    % To create MIDI output, uncomment the following line:
    %  \midi {\tempo 4 = 90 }
    }


\paper {
  tagline = ##f
}

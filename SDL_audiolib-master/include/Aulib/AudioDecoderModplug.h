// This is copyrighted software. More information is at the end of this file.
#pragma once

#include <Aulib/AudioDecoder.h>

namespace Aulib {

/*!
 * \brief ModPlug decoder.
 */
class AULIB_EXPORT AudioDecoderModPlug final: public AudioDecoder {
public:
    AudioDecoderModPlug();
    ~AudioDecoderModPlug() override;

    bool open(SDL_RWops* rwops) override;
    int getChannels() const override;
    int getRate() const override;
    bool rewind() override;
    float duration() const override;
    bool seekToTime(float seconds) override;

protected:
    int doDecoding(float buf[], int len, bool& callAgain) override;

private:
    const std::unique_ptr<struct AudioDecoderModPlug_priv> d;
};

} // namespace Aulib


/*

Copyright (C) 2014, 2015, 2016, 2017, 2018 Nikos Chantziaras.

This file is part of SDL_audiolib.

SDL_audiolib is free software: you can redistribute it and/or modify it under
the terms of the GNU Lesser General Public License as published by the Free
Software Foundation, either version 3 of the License, or (at your option) any
later version.

SDL_audiolib is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more
details.

You should have received a copy of the GNU Lesser General Public License
along with SDL_audiolib. If not, see <http://www.gnu.org/licenses/>.

*/

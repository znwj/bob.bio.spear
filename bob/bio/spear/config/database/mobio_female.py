#!/usr/bin/env python

import bob.db.verification.filelist
import bob.bio.base

mobio_wav_directory = "[YOUR_MOBIO_WAV_DIRECTORY]"
database = bob.bio.base.database.DatabaseBob(
    database = bob.db.verification.filelist.Database('bob/bio/spear/config/database/mobio/mobile0-female/',
        original_directory = mobio_wav_directory,
        original_extension = ".wav",
    ),
    name = "mobile0-female",
    protocol = '',
    
)

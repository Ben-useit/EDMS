from mayan.apps.dependencies.classes import PythonDependency

PythonDependency(
    legal_text='''
        Copyright (c) 2015 Ask Solem & contributors.  All rights reserved.
        Copyright (c) 2012-2014 GoPivotal, Inc.  All rights reserved.
        Copyright (c) 2009, 2010, 2011, 2012 Ask Solem, and individual contributors.  All rights reserved.

        Celery is licensed under The BSD License (3 Clause, also known as
        the new BSD license).  The license is an OSI approved Open Source
        license and is GPL-compatible(1).

        The license text can also be found here:
        http://www.opensource.org/licenses/BSD-3-Clause

        License
        =======

        Redistribution and use in source and binary forms, with or without
        modification, are permitted provided that the following conditions are met:
        * Redistributions of source code must retain the above copyright
        notice, this list of conditions and the following disclaimer.
        * Redistributions in binary form must reproduce the above copyright
        notice, this list of conditions and the following disclaimer in the
        documentation and/or other materials provided with the distribution.
        * Neither the name of Ask Solem, nor the
        names of its contributors may be used to endorse or promote products
        derived from this software without specific prior written permission.

        THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
        AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
        THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
        PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL Ask Solem OR CONTRIBUTORS
        BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
        CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
        SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
        INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
        CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
        ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
        POSSIBILITY OF SUCH DAMAGE.

        Documentation License
        =====================

        The documentation portion of Celery (the rendered contents of the
        "docs" directory of a software distribution or checkout) is supplied
        under the Creative Commons Attribution-Noncommercial-Share Alike 3.0
        United States License as described by
        http://creativecommons.org/licenses/by-nc-sa/3.0/us/

        Footnotes
        =========
        (1) A GPL-compatible license makes it possible to
        combine Celery with other software that is released
        under the GPL, it does not mean that we're distributing
        Celery under the GPL license.  The BSD license, unlike the GPL,
        let you distribute a modified version without making your
        changes open source.
    ''', module=__name__, name='celery', version_string='==5.4.0'
)
PythonDependency(
    legal_text='''
        Copyright (c) 2012-2013 GoPivotal, Inc.  All Rights Reserved.
        Copyright (c) 2009-2012 Ask Solem.  All Rights Reserved.
        All rights reserved.

        Redistribution and use in source and binary forms, with or without
        modification, are permitted provided that the following conditions are met:

        * Redistributions of source code must retain the above copyright notice,
        this list of conditions and the following disclaimer.
        * Redistributions in binary form must reproduce the above copyright
        notice, this list of conditions and the following disclaimer in the
        documentation and/or other materials provided with the distribution.

        Neither the name of Ask Solem nor the names of its contributors may be used
        to endorse or promote products derived from this software without specific
        prior written permission.

        THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
        AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
        THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
        PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL Ask Solem OR CONTRIBUTORS
        BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
        CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
        SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
        INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
        CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
        ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
        POSSIBILITY OF SUCH DAMAGE.

        Documentation License
        =====================

        The documentation portion of django-celery-beat (the rendered contents of the
        "docs" directory of a software distribution or checkout) is supplied
        under the "Creative Commons Attribution-ShareAlike 4.0
        International" (CC BY-SA 4.0) License as described by
        http://creativecommons.org/licenses/by-sa/4.0/

        Footnotes
        =========
        (1) A GPL-compatible license makes it possible to
            combine django-celery-beat with other software that is released
            under the GPL, it does not mean that we're distributing
            django-celery-beat under the GPL license.  The BSD license, unlike the GPL,
            let you distribute a modified version without making your
            changes open source.
    ''', module=__name__, name='django-celery-beat', version_string='==2.7.0'
)

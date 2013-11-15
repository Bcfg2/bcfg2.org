Home
####

:date: 2013-07-01
:url:  
:save_as: index.html

Bcfg2 helps system administrators produce a consistent, reproducible, and
verifiable description of their environment, and offers visualization and
reporting tools to aid in day-to-day administrative tasks. It is the fifth
generation of configuration management tools developed in the `Mathematics and
Computer Science Division of Argonne National Laboratory`_.

It is based on an operational model in which the specification can be used to
validate and optionally change the state of clients, but in a feature unique to
Bcfg2 the client's response to the specification can also be used to assess the
completeness of the specification. Using this feature, Bcfg2 provides an
objective measure of how good a job an administrator has done in specifying the
configuration of client systems. Bcfg2 is therefore built to help
administrators construct an accurate, comprehensive specification.

Bcfg2 has been designed from the ground up to support gentle reconciliation
between the specification and current client states. It is designed to
gracefully cope with manual system modifications.

Finally, due to the rapid pace of updates on modern networks, client systems
are constantly changing; if required in your environment, Bcfg2 can enable the
construction of complex change management and deployment strategies.

Bcfg2 is fairly portable. It has been successfully run on:

* AIX_, FreeBSD_, OpenBSD_, `Mac OS X`_, OpenSolaris_, Solaris_
* Many `GNU/Linux`_ distributions, including `Alpine Linux`_, ArchLinux_, Blag_, CentOS_, Debian_, Fedora_, Gentoo_, gNewSense_, Mandriva_, openSUSE_, `Red Hat/RHEL`_, `SuSE/SLES`_, Trisquel_, and Ubuntu_.

Bcfg2 should run on any POSIX compatible operating system, however direct
support for an operating system's package and service formats are limited by
the currently available `client tools`_ (new client tools are pretty easy to add).
There is also an `incomplete but more exact list of platforms on which Bcfg2 works`_.


.. _`Mathematics and Computer Science Division of Argonne National Laboratory`: http://www.mcs.anl.gov
.. _AIX: http://www.ibm.com/aix
.. _FreeBSD: http://www.freebsd.org/
.. _OpenBSD: http://www.openbsd.org/
.. _`Mac OS X`: http://www.apple.com/macosx/
.. _OpenSolaris: http://opensolaris.org/
.. _Solaris: http://www.oracle.com/solaris/
.. _`GNU/Linux`: http://www.gnu.org/gnu/linux-and-gnu.html
.. _`Alpine Linux`: http://www.alpinelinux.org/
.. _ArchLinux: http://www.archlinux.org/
.. _Blag: http://www.blagblagblag.org/
.. _CentOS: http://www.centos.org/
.. _Debian: http://www.debian.org/
.. _Fedora: http://fedoraproject.org/
.. _Gentoo: http://www.gentoo.org/
.. _gNewSense: http://www.gnewsense.org/
.. _Mandriva: http://www.mandriva.com/
.. _openSUSE: http://www.opensuse.org/
.. _`Red Hat/RHEL`: http://www.redhat.com/rhel/
.. _`SuSE/SLES`: http://www.novell.com/linux
.. _Trisquel: http://trisquel.info/
.. _Ubuntu: http://www.ubuntu.com/
.. _`client tools`: http://docs.bcfg2.org/dev/client/tools.html
.. _`incomplete but more exact list of platforms on which bcfg2 works`: http://trac.mcs.anl.gov/projects/bcfg2/wiki/EncapPlatforms


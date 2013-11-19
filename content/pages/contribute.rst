==========
Contribute
==========

There are several ways users can contribute to the Bcfg2 project. 

 * Developing code
 * Testing pre-releases
 * Adding to the common repository
 * Improving the wiki
 * Writing documentation
 * Reporting bugs

Development
===========

There are several methods for submitting patches. You can send the patch
to the `Bcfg2 mailing list <{filename}/pages/mailinglist.rst>`_, create
a trac `ticket <https://trac.mcs.anl.gov/projects/bcfg2/newticket>`_
with the patch included, or submit a pull request on
`github`_. In order to submit a ticket via the trac system, you
will need to create a session by clicking on the `Preferences
<https://trac.mcs.anl.gov/projects/bcfg2/prefs>`_ link and filling
out/saving changes to the form. In order to be considered for mainline
inclusion, patches need to be BSD licensed.

The `web interface <http://git.mcs.anl.gov/bcfg2.git/>`_
to the git repository, `github`_ or the `source browser
<http://trac.mcs.anl.gov/projects/bcfg2/browser/>`_ can give you
an overview of the source code.  For more details about the usage
of the git repository, please refer to the `Submitting Patches
<http://docs.bcfg2.org/dev/development/submitting-patches.html>`_ page.

.. _`github`: https://github.com/Bcfg2/bcfg2

Several resources for developers exist at http://docs.bcfg2.org/development/.

Bcfg2 is the result of a lot of work by many different people. They are
listed on the `contributors page <{filename}/pages/contributors.rst>`_.

Testing Prereleases
===================

Before each release, several prereleases will be tagged. It is helpful
to have users test these releases (when feasible) because it is hard to
replicate the full range of potential reconfiguration situations; between
different operating systems, system management tools, and configuration
specification variation, there can be large differences between sites.

Adding to the Common Repository
===============================

The Bcfg2 common repository is a set of portable examples that new
repositories can be based on. This repo has several parts. The first
is a series of group definitions that describe a wide range of client
systems. The second is a set of portable bundles that have been ported
to use these groups. This makes these bundles transparently portable
across new client architectures.

This approach has several benefits to users

 * Configuration specification can be shared across sites where appropriate
 * This common configuration specification can be reused, allowing
   sites to migrate to new systems that other sites have already ported
   the common repository to
 * Setup of new systems becomes a lot easier.

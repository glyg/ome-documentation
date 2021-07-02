#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# ome documentation build configuration file, created by
# sphinx-quickstart on Wed Feb 22 20:24:38 2012.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys
import os
import shutil

# Append the top level directory of the docs, so we can import from the
# config dir.
sys.path.insert(0, os.path.abspath('../common'))
from conf import *
sys.path.insert(1, os.path.abspath('../omero'))
import conf_autogen


# -- General configuration ----------------------------------------------------

# General information about the project.
project = u'OMERO'
title = project + u' Documentation'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
if "OMERO_RELEASE" in os.environ and len(os.environ.get('OMERO_RELEASE')) > 0:
    release = os.environ.get('OMERO_RELEASE')
    [majornumber, minornumber, patchnumber] = split_release(release)

    # Define Sphinx version and release variables and development branch
    version = ".".join(str(x) for x in (majornumber, minornumber))

    if patchnumber > 0:
        tags.add('point_release')
    previousversion = get_previous_version(majornumber, minornumber)
else:
    version = 'UNKNOWN'
    previousversion = 'UNKNOWN'
    release = 'UNKNOWN'

rst_prolog = """
"""

rst_epilog += """
.. |OmeroPy| replace:: :doc:`/developers/Python`
.. |OmeroCpp| replace:: :doc:`/developers/Cpp`
.. |OmeroJava| replace:: :doc:`/developers/Java`
.. |OmeroMatlab| replace:: :doc:`/developers/Matlab`
.. |OmeroApi| replace:: :doc:`/developers/Modules/Api`
.. |OmeroWeb| replace:: :doc:`/developers/Web`
.. |OmeroClients| replace:: :doc:`/developers/GettingStarted`
.. |OmeroGrid| replace:: :doc:`/sysadmins/grid`
.. |OmeroSessions| replace:: :doc:`/developers/Server/Sessions`
.. |OmeroModel| replace:: :doc:`/developers/Model`
.. |ExtendingOmero| replace:: :doc:`/developers/Server/ExtendingOmero`
.. |BlitzGateway| replace:: :doc:`/developers/Python`
.. |DevelopingOmeroClients| replace:: :doc:`/developers/GettingStarted/AdvancedClientDevelopment`
.. _Spring: https://spring.io
.. |previousversion| replace:: %s
.. |current_dbver|  replace:: %s
.. |previous_dbver|  replace:: %s
.. |version_py|  replace:: %s
.. |version_web|  replace:: %s
.. |iceversion| replace:: 3.6.5
.. |postgresversion| replace:: 11
.. |javaversion| replace:: 11
.. |javaversion_min| replace:: 8
.. |version_dropbox|  replace:: %s

.. |Broken| image:: /images/broken.png
             :alt: Broken
.. |Deprecated| image:: /images/deprecated.png
                 :alt: Deprecated
.. |Dropped| image:: /images/dropped.png
              :alt: Dropped
.. |Recommended| image:: /images/recommended.png
                  :alt: Recommended
.. |Supported| image:: /images/supported.png
                :alt: Supported
.. |Unsupported| image:: /images/unsupported.png
                  :alt: Unsupported
.. |Upcoming| image:: /images/upcoming.png
               :alt: Upcoming
""" % (previousversion, conf_autogen.current_dbver,
       conf_autogen.previous_dbver,
       conf_autogen.version_py,
       conf_autogen.version_web,
       conf_autogen.version_dropbox)

omero_subs_github_root = github_root + 'ome/{}/{}/{}/%s'

# OMERO-specific extlinks
omero_extlinks = {
    # GitHub links
    'source': (omero_github_root + 'blob/'+ branch + '/%s', ''),
    'sourcedir': (omero_github_root + 'tree/' + branch + '/%s', ''),
    'commit': (omero_github_root + 'commit/%s', ''),
    'omedocs': (doc_github_root + '%s', ''),
    # GitHub decoupled subcomponents
    'omero_subs_github_repo_root': (github_root + 'ome/%s', ''),
    'dsl_plugin_source': (omero_subs_github_root.format('omero-dsl-plugin', 'blob', 'v' + conf_autogen.version_dsl_plugin), ''),
    'dsl_plugin_sourcedir': (omero_subs_github_root.format('omero-dsl-plugin', 'tree', 'v' + conf_autogen.version_dsl_plugin), ''),
    'blitz_plugin_source': (omero_subs_github_root.format('omero-blitz-plugin', 'blob', 'v' + conf_autogen.version_blitz_plugin), ''),
    'blitz_plugin_sourcedir': (omero_subs_github_root.format('omero-blitz-plugin', 'tree', 'v' + conf_autogen.version_blitz_plugin), ''),
    'ice_builder_source': (omero_subs_github_root.format('ice-builder-gradle', 'blob', 'v' + conf_autogen.version_ice_builder), ''),
    'ice_builder_sourcedir': (omero_subs_github_root.format('ice-builder-gradle', 'tree', 'v' + conf_autogen.version_ice_builder), ''),
    'model_source': (omero_subs_github_root.format('omero-model', 'blob', 'v' + conf_autogen.version_model), ''),
    'model_sourcedir': (omero_subs_github_root.format('omero-model', 'tree', 'v' + conf_autogen.version_model), ''),
    'common_source': (omero_subs_github_root.format('omero-common', 'blob', 'v' + conf_autogen.version_common), ''),
    'common_sourcedir': (omero_subs_github_root.format('omero-common', 'tree', 'v' + conf_autogen.version_common), ''),
    'romio_source': (omero_subs_github_root.format('omero-romio', 'blob', 'v' + conf_autogen.version_romio), ''),
    'romio_sourcedir': (omero_subs_github_root.format('omero-romio', 'tree', 'v' + conf_autogen.version_romio), ''),
    'renderer_source': (omero_subs_github_root.format('omero-renderer', 'blob', 'v' + conf_autogen.version_renderer), ''),
    'renderer_sourcedir': (omero_subs_github_root.format('omero-renderer', 'tree', 'v' + conf_autogen.version_renderer), ''),
    'server_source': (omero_subs_github_root.format('omero-server', 'blob', 'v' + conf_autogen.version_server), ''),
    'server_sourcedir': (omero_subs_github_root.format('omero-server', 'tree', 'v' + conf_autogen.version_server), ''),
    'blitz_source': (omero_subs_github_root.format('omero-blitz', 'blob', 'v' + conf_autogen.version_blitz), ''),
    'blitz_sourcedir': (omero_subs_github_root.format('omero-blitz', 'tree', 'v' + conf_autogen.version_blitz), ''),
    'java_gateway_source': (omero_subs_github_root.format('omero-gateway-java', 'blob', 'v' + conf_autogen.version_gateway), ''),
    'java_gateway_sourcedir': (omero_subs_github_root.format('omero-gateway-java', 'tree', 'v' + conf_autogen.version_gateway), ''),
    'matlab_source': (omero_subs_github_root.format('omero-matlab', 'blob', 'v' + conf_autogen.version_matlab), ''),
    'matlab_sourcedir': (omero_subs_github_root.format('omero-matlab', 'tree', 'v' + conf_autogen.version_matlab), ''),
    'insight_source': (omero_subs_github_root.format('omero-insight', 'blob', 'master'), ''),
    'insight_sourcedir': (omero_subs_github_root.format('omero-insight', 'tree', 'master'), ''),
    'web_source': (omero_subs_github_root.format('omero-web', 'blob', 'v' + conf_autogen.version_web), ''),
    'web_sourcedir': (omero_subs_github_root.format('omero-web', 'tree', 'v' + conf_autogen.version_web), ''),
    'py_source': (omero_subs_github_root.format('omero-py', 'blob', 'v' + conf_autogen.version_py), ''),
    'py_sourcedir': (omero_subs_github_root.format('omero-py', 'tree', 'v' + conf_autogen.version_py), ''),
    'dropbox_source': (omero_subs_github_root.format('omero-dropbox', 'blob', 'v' + conf_autogen.version_dropbox), ''),
    'dropbox_sourcedir': (omero_subs_github_root.format('omero-dropbox', 'tree', 'v' + conf_autogen.version_dropbox), ''),
    # API links
    'javadoc': (downloads_root + '/latest/omero5.5/api/%s', ''),
    'javadoc_gateway_java': (docs_root + '/omero-gateway/' + conf_autogen.version_gateway + '/javadoc/%s', ''),
    'javadoc_blitz': (docs_root + '/omero-blitz/' + conf_autogen.version_blitz + '/javadoc/%s', ''),
    'javadoc_server': (docs_root + '/omero-server/' + conf_autogen.version_server + '/javadoc/%s', ''),
    'javadoc_renderer': (docs_root + '/omero-renderer/' + conf_autogen.version_renderer + '/javadoc/%s', ''),
    'javadoc_romio': (docs_root + '/omero-romio/' + conf_autogen.version_romio + '/javadoc/%s', ''),
    'javadoc_common': (docs_root + '/omero-common/' + conf_autogen.version_common + '/javadoc/%s', ''),
    'javadoc_model': (docs_root + '/omero-model/' + conf_autogen.version_model + '/javadoc/%s', ''),
    'slicedoc_blitz': (docs_root + '/omero-blitz/' +
                       conf_autogen.version_blitz + '/slice2html/%s', ''),
    'pythondoc': (downloads_root + '/latest/omero5.5/api/python/%s', ''),
    # Downloads
    'downloads': (downloads_root + '/latest/omero5.5/%s', ''),
    # Versioned Bio-Formats doc link
    'bf_v_doc': (docs_root + '/bio-formats/' + conf_autogen.version_bioformats + '/' + '%s', ''),
    # Miscellaneous links
    'springdoc': ('https://docs.spring.io/spring/docs/%s', ''),
    'ivydoc': ('https://ant.apache.org/ivy/history/2.3.0/%s', ''),
    }
extlinks.update(omero_extlinks)

# Edit on GitHub prefix
edit_on_github_prefix = 'omero'

# -- Options for HTML output --------------------------------------------------

# Custom sidebar templates, maps document names to template names.
html_sidebars['**'].insert(1, 'globalomerotoc.html')

# Add any paths that contain custom themes here, relative to this directory.
html_theme_path.extend(['themes'])

# -- Options for LaTeX output -------------------------------------------------

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual])
# target = project + '-' + release + '.tex'
# latex_documents = [
#  (master_doc, target, title, author, 'manual'),
# ]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
# latex_logo = 'images/omero-logo.pdf'

# -- Options for the linkcheck builder ----------------------------------------

# Regular expressions that match URIs that should not be checked when doing a
# linkcheck build
linkcheck_ignore += [
    r'http://localhost:\d+/?', 'http://localhost/',
    'http://www.hibernate.org',
    'https://www.jboss.org',
    'https://code.google.com/archive/p/luke/',
    'https://www.youtube.com/channel/UCyySB9ZzNi8aBGYqcxSrauQ',
    'https://httpd.apache.org/docs/current/mod/mod_proxy.html',
    'https://access.redhat.com/articles/3078',
    r'.*[.]sourceforge.net',
    r'https?://www\.openmicroscopy\.org/site/team/.*',
    r'.*[.]?example\.com/.*',
    r'https://spreadsheets.google.com/.*',
    r'https://msdn.microsoft.com/en-us/library/aa362244\(v=vs.85\).aspx',
    'https://testng.org/',
    'https://packages.ubuntu.com/search',
    # Those below may start working with Sphinx 2.1, see sphinx-doc #6381.
    'https://www.cloudflare.com/',
    'https://www.zenoss.com/',
    # Timeouts which may be fixed in a newer version
    'https://micronoxford.com/',
    github_root + 'ome/',
    r'https://help.openmicroscopy.org/.*#.*']

exclude_patterns = ['sysadmins/unix/walkthrough/requirements*',
                    'downloads/inplace', 'downloads/cli',
                    'changelog.rst']


def copy_legacy_redirects(app, exception):
    """
    see: https://tech.signavio.com/2017/managing-sphinx-redirects
    """
    print("Adding redirects:")
    redirect_files = [
        'sysadmins/server-overview.html',
        'sysadmins/server-tables.html',
        'sysadmins/omero-home-prefix.html',
        'sysadmins/install-web.html',
        'developers/Insight/Architecture.html',
        'developers/Insight/Configuration.html',
        'developers/Insight/DirectoryContents.html',
        'developers/Insight/EventBus.html',
        'developers/Insight/HowTo/BuildAgent.html',
        'developers/Insight/HowTo/BuildAgentView.html',
        'developers/Insight/HowTo/RetrieveData.html',
        'developers/Insight/ImplementationView.html',
        'developers/Insight/TaskBar.html',

    ]
    if app.builder.name == 'html':
        for html_src_path in redirect_files:
            target_path = app.outdir + '/' + html_src_path
            src_path = app.srcdir + '/' + html_src_path
            if os.path.isfile(src_path):
                target_dir = os.path.dirname(target_path)
                if not os.path.exists(target_dir):
                    os.makedirs(target_dir)
                shutil.copyfile(src_path, target_path)
                print("  %s" % html_src_path)


def setup(app):
    app.connect('build-finished', copy_legacy_redirects)

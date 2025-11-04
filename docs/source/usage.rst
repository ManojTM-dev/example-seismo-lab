Usage
=====

.. _installation:

Installation
------------

Follow these steps to set up the **TIFF–GDAL Docs** project locally.

1. Clone the Repository
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: console

   $ cd ~
   $ git clone https://github.com/ManojTM-dev/tiff-gdal-docs.git
   $ cd tiff-gdal-docs

2. Create a Python Environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

It’s best to isolate the environment to avoid dependency conflicts.

.. code-block:: console

   $ conda create -n docs_env python=3.8
   $ conda activate docs_env

3. Install Python Dependencies
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Install the required packages listed in the documentation’s `requirements.txt`.

.. code-block:: console

   $ pip install -r docs/requirements.txt

4. Install GDAL and GMT
~~~~~~~~~~~~~~~~~~~~~~~

These libraries are essential for geospatial and raster operations.

.. code-block:: console

   $ conda install -c conda-forge gdal
   $ conda install -c conda-forge gmt=6.0.0

5. Verify Installations
~~~~~~~~~~~~~~~~~~~~~~~

Check that both GDAL and GMT are correctly installed.

.. code-block:: console

   $ gdalinfo --version
   $ gmt --version

System Compatibility
~~~~~~~~~~~~~~~~~~~~

This setup matches the environment used on **Read the Docs**:

- **OS:** Ubuntu 20.04  
- **Python:** 3.8  
- **GMT:** 6.0.0  
- **GDAL:** via conda-forge


## Description
This project publishes my resume to a staticwebsite hosted on Azure.  The workflow consists of taking my ./src/resume.md file and then converting into a static site which is published to Azure.

## Iconography
I want to use icons from fontawesome specifically for contact information section.

## Source
The resume is currently defined as a YAML file at ./src/content.yaml.  I want to use this file to generate static html which then can be deployed via pipeline to https://jasonbrisbin.com

## Workflow
After any formatting or content change, always prompt me to run the /build command and then open dist/index.html in the browser so I can preview the result.

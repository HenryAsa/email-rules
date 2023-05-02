# `email-rules`
`email-rules` is a repository to build Email Rules and Filters to help you organize your inbox.

## Table of Contents:
- [Purpose](#purpose)
- [Documentation](#documentation)
- [Currently Supported Email Clients](#currently-supported-email-clients)
- [Email Clients to be Supported in the Future](#email-clients-to-be-supported-in-the-future)

Purpose:
--------

Rather than using the clunky UIs of multiple different email clients, `email-rules` enables you to write your rules using Python and then generate client-compatible representations of your rules, so they can be enforced.  This repository enables you to have a single source for all of your rules, and allows you to generate rules in a streamlined manner.  Additionally, if you decide to switch email clients in the future, you will be able to copy over all of your email rules without having to manually (and painstakingly) rewrite them for each email client you use.

Documentation:
--------------
Documentation outlining how to use this repository can be [found here](https://henryasa.github.io/email-rules/).  I used [`NumPy` Documentation Standard](https://numpydoc.readthedocs.io/en/latest/format.html) to outline the functionality of my code, and used [`sphinx`](https://www.sphinx-doc.org/en/master/) to generate the [docs website](https://henryasa.github.io/email-rules/).

Currently Supported Email Clients:
----------------------------------
- Gmail
> While Gmail is the only supported email client right now, this will change in the future.  See [Email Clients to be Supported in the Future](#email-clients-to-be-supported-in-the-future) for more details.

Email Clients to be Supported in the Future:
--------------------------------------------
- Microsoft Outlook
- Mac Mail
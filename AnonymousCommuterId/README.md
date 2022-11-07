AnonymousId Smart Data Model
============================

This is model is intented to be used when some PII tracking is needed, and thus it's needed to anonimize the identifiers
in order to still provide some useful insights, but using a non-reversible anonymizing (hashing) function.

As it is ussually the case, there are provisioned standarized attributes to indicate the current and previous location
of the detection. They are intented to hold another entity ID, because having the detectors also replicated in the form
of entities provides a much better data modelling experience.

Finally, an algorithm attribute was added in order to aid with the several ways and methodologies of anonymizing PII.

About
-----------------
This model was contributed by Purple Blob S.L., and tailored according to the views and necessities of our METIS anonymized
people flow product. We are open about the development of a wide use AnonymousId interoperable data model, and thus,
feel free to contact adelgado@purpleblob.net or iruiz@purpleblob.net for additional discussion, or even better, open a 
Github Issue!

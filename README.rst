Django Snippets Cream
=====================

Django app packaging the best snippets found on http://djangosnippets.org


Included Snippets
-----------------

Resolve URLs to View Name
+++++++++++++++++++++++++
Suplies a resolve_to_name function that takes in a path and resolves it to a view name or view function name (given that the path is actually defined in your urlconf).

Original Snippet - http://djangosnippets.org/snippets/1378/

Example::

    === urlconf ====
    urlpatterns = patterns(''
        (r'/some/url', 'app.views.view'),
        (r'/some/other/url', 'app.views.other.view', {}, 'this_is_a_named_view'),
    )

    === example usage in interpreter ===
    >>> from snippetscream import resolve_to_name
    >>> print resolve_to_name('/some/url')
    'app.views.view'
    >>> print resolve_to_name('/some/other/url')
    'this_is_a_named_view'

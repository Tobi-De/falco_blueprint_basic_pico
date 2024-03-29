def sentry_traces_sampler(sampling_context):
    """
    Returns an int representing the probability of a trace being sampled.

    Disregards any health check requests.
    """
    if _should_disgard(sampling_context):
        return 0

    return 0.5


def sentry_profiles_sampler(sampling_context):
    """
    Returns an int representing the probability of a profile being sampled.

    Disregards any health check requests.
    """
    if _should_disgard(sampling_context):
        return 0

    return 0.5


def _should_disgard(sampling_context) -> bool:
    disgarded_methods = ["GET", "HEAD"]
    disgarded_paths = ["/health/"]

    return (
        sampling_context.get("wsgi_environ", None)
        and sampling_context["wsgi_environ"]["REQUEST_METHOD"] in disgarded_methods
        and sampling_context["wsgi_environ"]["PATH_INFO"] in disgarded_paths
    )

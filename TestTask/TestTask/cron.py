from django_cron import CronJobBase, Schedule

from news.models import Post


class ResetPostUpvote(CronJobBase):
    """
    Reset all post upvote to zero every day 
    """

    RUN_EVERY_MINS = 60 * 24
    RETRY_AFTER_FAILURE_MINS = 5
    ALLOW_PARALLEL_RUNS = True
    schedule = Schedule(
        run_every_mins=RUN_EVERY_MINS, retry_after_failure_mins=RETRY_AFTER_FAILURE_MINS
    )

    code = "TestTask.reset_postupvote"

    def do(self):
        Post.objects.filter(amount_of_upvotes__gt=0).update(amount_of_upvotes=0)

from django.db import models


class Criminal(models.Model):
    criminal_id = models.AutoField(primary_key=True)

    last_name = models.CharField(max_length=15)
    first_name = models.CharField(max_length=10)

    street = models.CharField(max_length=30)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=2)
    zip = models.CharField(max_length=5)

    phone = models.CharField(max_length=10)

    v_status = models.CharField(max_length=1, default='N')  # violet_offender_status
    p_status = models.CharField(max_length=1, default='N')  # probation_status


class Alias(models.Model):
    alias_id = models.AutoField(primary_key=True)
    criminal_id = models.ForeignKey(Criminal, on_delete=models.CASCADE, default=0)

    alias = models.CharField(max_length=20)


class Crime(models.Model):
    crime_id = models.AutoField(primary_key=True)
    criminal_id = models.ForeignKey(Criminal, on_delete=models.CASCADE)

    classification = models.CharField(max_length=1, default='U')
    date_charged = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=2)
    hearing_date = models.DateField(null=True, blank=True)
    appeal_cut_date = models.DateField(null=True, blank=True)

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=models.Q(hearing_date__gt=models.F('date_charged')),
                name='hearing_date_gt_date_charged'
            ),
        ]


class ProbationOfficer(models.Model):
    prob_id = models.AutoField(primary_key=True)

    last_name = models.CharField(max_length=15)
    first_name = models.CharField(max_length=10)

    street = models.CharField(max_length=30)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=2)
    zip = models.CharField(max_length=5)

    phone = models.CharField(max_length=10)
    email = models.EmailField(max_length=30)
    status = models.CharField(max_length=1)


class Sentence(models.Model):
    sentence_id = models.AutoField(primary_key=True)
    criminal_id = models.ForeignKey(Criminal, on_delete=models.CASCADE)

    type = models.CharField(max_length=1)
    prob_officer = models.ForeignKey(ProbationOfficer, on_delete=models.CASCADE, db_column='prob_id')

    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    violations = models.IntegerField()

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=models.Q(end_date__gt=models.F('start_date')),
                name='end_date_gt_start_date'
            ),
        ]


class CrimeCodes(models.Model):
    crime_code = models.AutoField(primary_key=True)
    code_description = models.CharField(max_length=30, unique=True)


class CrimeCharge(models.Model):
    charge_id = models.AutoField(primary_key=True)
    crime_id = models.ForeignKey(Crime, on_delete=models.CASCADE)
    crime_code = models.ForeignKey(CrimeCodes, on_delete=models.CASCADE)

    charge_status = models.CharField(max_length=2)
    fine_amount = models.IntegerField(null=True, blank=True)
    court_fee = models.IntegerField(null=True, blank=True)
    amount_paid = models.IntegerField(null=True, blank=True)
    pay_due_date = models.DateField(null=True, blank=True)


class Officer(models.Model):
    officer_id = models.AutoField(primary_key=True)

    last_name = models.CharField(max_length=15)
    first_name = models.CharField(max_length=10)

    precinct = models.CharField(max_length=4)
    badge = models.CharField(max_length=14, unique=True)

    phone = models.CharField(max_length=10)
    status = models.CharField(max_length=1, default='A')


class CrimeOfficer(models.Model):
    crime_id = models.ForeignKey(Crime, on_delete=models.CASCADE)
    officer_id = models.ForeignKey(Officer, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['crime_id', 'officer_id'], name='primary_key'),
        ]


class Appeal(models.Model):
    appeal_id = models.AutoField(primary_key=True)
    crime_id = models.ForeignKey(Crime, on_delete=models.CASCADE)

    filing_date = models.DateField(null=True, blank=True)
    hearing_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=1, default='P')

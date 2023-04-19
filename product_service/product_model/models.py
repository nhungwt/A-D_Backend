# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True, default="", 
                            help_text='Unique value for product page URL, created from name')
    image = models.CharField(max_length=500, null=True)
    description = models.TextField()
    urlService = models.CharField(max_length=255, null=True) # URL that Service provide

    class Meta:
        db_table = 'category'
        ordering = ['name']
        # Khắc phục việc hiển thị số nhiều
        # Djnago sẽ tự động hiển thị số nhiều bằng cách thêm 's'
        # Dòng code dưới nhằm ghi đè lên, thay vì 'Categorys' ->> 'Categories'
        verbose_name_plural = 'Categories'

    # returning a string representation of Category model (vì khi in 1 obj, nó trả về toàn thông tin ko đâu ấy)
    # được gọi bất cứ khi nào tham chiếu tới đối tượng của model, trong đây custom cái được trả về, dùng {} cũng được
    def __str__(self):
        return self.name

    # Thông báo cho django biết method này dùng để tạo liên kết (permalink) (dùng khi xác định dùng slug)
    # Bất cứ khi nào gọi method này trong template, link sẽ được khởi tạo từ urls.py để ánh xạ
    def get_absolute_url(self):
        print("Đang gọi tới hàm get_absolute_url trong product/model.py.........")
        return reverse('catalog_category', kwargs={'category_slug', self.slug})


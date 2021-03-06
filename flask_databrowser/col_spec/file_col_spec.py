# -*- coding: utf-8 -*-
from flask_upload2.fields import FileField
from .col_spec import ColSpec


class FileColSpec(ColSpec):

    as_input = True
    disabled = False

    def __init__(self, col_name, label=None, validators=None, save_path=None,
                 doc=None, max_num=1):
        '''
        :param save_path: string of function, which accepts 2 parameters, record and
            filename, if not specified, file will be saved in model view's upload
            folder with a random file name or original file name, which is
            determined by `ModelView.override_upload_filename`

            .. code::python

                function (record, filename):
                    return str(record.id) + '_' + filename

        :param max_num: maximum number of files allowed to be uploaded

        '''
        super(FileColSpec, self).__init__(col_name, label=label, doc=doc)
        self.validators = validators or []
        self.save_path = save_path
        self.max_num = max_num

    def make_field(self, record=None, model_view=None):
        return FileField(save_path=self.save_path, max_num=self.max_num,
                         id=self.col_name,
                         validators=self.validators,
                         label=self.label, description=self.doc)

    @property
    def remote_create_url(self):
        return None

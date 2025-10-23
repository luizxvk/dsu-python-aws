FROM public.ecr.aws/lambda/python:3.12

# Instala dependências nativas do WeasyPrint
RUN yum install -y \
    cairo cairo-devel \
    pango pango-devel \
    gdk-pixbuf2 gdk-pixbuf2-devel \
    freetype freetype-devel \
    libjpeg-turbo libjpeg-turbo-devel \
    libpng libpng-devel \
    libffi libffi-devel \
    && yum clean all

# Copia código
COPY . /var/task

# Instala dependências Python
COPY requirements.txt /var/task/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["main.lambda_handler"]

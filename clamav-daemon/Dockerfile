FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y clamav clamav-daemon && \
    # Fix clamd.conf to listen on all interfaces and port 3310
    sed -i 's/^#\?TCPSocket .*/TCPSocket 3310/' /etc/clamav/clamd.conf && \
    sed -i 's/^#\?TCPAddr .*/TCPAddr 0.0.0.0/' /etc/clamav/clamd.conf && \
    sed -i 's/^Example/#Example/' /etc/clamav/clamd.conf && \
    # Prepare runtime directory with correct ownership
    mkdir -p /var/run/clamav && \
    chown clamav:clamav /var/run/clamav && \
    # Update virus definitions
    freshclam

EXPOSE 3310

CMD ["clamd", "--foreground", "-c", "/etc/clamav/clamd.conf"]

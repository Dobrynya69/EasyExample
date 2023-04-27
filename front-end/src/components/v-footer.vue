<script>

</script>
<template>
    <footer class="footer">
        <div class="footer__content">
            <div class="copyright">
                @site
            </div>
            <div class="contacts">
                <div class="contacts__text">Contacts</div>
                <div class="contacts__data">
                    <div class="tel">tel:+380980944511</div>
                    <div class="mail">email: email.ore</div>
                </div>
            </div>
        </div>
    </footer>
</template>
<style>
.footer {
    background-color: #292929;
    width: 100%;
    height: 60px;
    position: relative;
    z-index: 10;
}
.footer__content {
    display: flex;
    justify-content: space-between;
    align-items: center;
    height: 100%;
    font-size: 20px;
    padding: 0px 20px;
    max-width: calc(1140px - 40px);
    margin: 0 auto;
    color: #fff;
}
.contacts {
    display: flex;
    align-items: center;
}   
.contacts__text {
    margin-right: 20px;
}
.contacts__data {
    display: flex;
    flex-direction: column;
    font-size: 16px;
}
.contacts__data div{
    text-decoration: underline;
}
</style>

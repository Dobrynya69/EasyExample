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
    background-color: #D9D9D9;
    padding: 10px;
    width: calc(100% - 20px);
    height: 60px;
}
.footer__content {
    display: flex;
    justify-content: space-between;
    align-items: center;
    height: 100%;
    font-size: 20px;
}
.contacts {
    display: flex;
    align-items: center;
}
.contacts__text {
    margin-right: 5px;
}
.contacts__data {
    display: flex;
    flex-direction: column;
    font-size: 16px;
}
</style>
